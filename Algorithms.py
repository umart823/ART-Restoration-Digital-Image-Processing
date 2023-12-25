import cv2
import bm3d
import numpy as np
import cv2
import os
import numpy as np
import cv2
from scipy.signal import convolve2d

def FastNlMeans_Denoising(imgPath,h,templateWindowSize,searchWindowSize):
    image = cv2.imread(imgPath)
    return cv2.fastNlMeansDenoising(image, None, h=10, templateWindowSize=7, searchWindowSize=21)

def BM3D_Denoising(imgPath,sigma):
    image = cv2.imread(imgPath)
    if len(image.shape) == 3:
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    else:
        gray_image = image

    denoised_image = bm3d.bm3d(gray_image, sigma_psd=sigma, stage_arg=bm3d.BM3DStages.ALL_STAGES)
    return denoised_image

def MedianBlur_Denoising(imgPath, kSize=5):
    image = cv2.imread(imgPath)
    return cv2.medianBlur(image,kSize)

def Colorize(imgPath):
    DIR = r"Colorization model"
    PROTOTXT = os.path.join(DIR, r"colorization_deploy_v2.prototxt")
    POINTS = os.path.join(DIR, r"pts_in_hull.npy")
    MODEL = os.path.join(DIR, r"colorization_release_v2.caffemodel")
    
    net = cv2.dnn.readNetFromCaffe(PROTOTXT, MODEL)
    pts = np.load(POINTS)

    class8 = net.getLayerId("class8_ab")
    conv8 = net.getLayerId("conv8_313_rh")
    pts = pts.transpose().reshape(2, 313, 1, 1)
    net.getLayer(class8).blobs = [pts.astype("float32")]
    net.getLayer(conv8).blobs = [np.full([1, 313], 2.606, dtype="float32")]

    # Load the input image
    image = cv2.imread(imgPath)
    scaled = image.astype("float32") / 255.0
    lab = cv2.cvtColor(scaled, cv2.COLOR_BGR2LAB)

    resized = cv2.resize(lab, (224, 224))
    L = cv2.split(resized)[0]
    L -= 50

    net.setInput(cv2.dnn.blobFromImage(L))
    ab = net.forward()[0, :, :, :].transpose((1, 2, 0))

    ab = cv2.resize(ab, (image.shape[1], image.shape[0]))

    L = cv2.split(lab)[0]
    colorized = np.concatenate((L[:, :, np.newaxis], ab), axis=2)

    colorized = cv2.cvtColor(colorized, cv2.COLOR_LAB2BGR)
    colorized = np.clip(colorized, 0, 1)

    colorized = (255 * colorized).astype("uint8")
    return colorized

def Richardson_lucy_blind_deconvolution_psf(imgPath, num_iterations=10, psf_size=(5, 5)):
    image = cv2.imread(imgPath)
    # Initialize the PSF and deblurred image
    psf = np.ones(psf_size) / np.prod(psf_size)
    deblurred_image = image.copy()

    for _ in range(num_iterations):
        # Estimate the blurred image using the current PSF
        blurred_estimate = convolve2d(deblurred_image, psf, 'same', 'symm')

        # Compute the error between the original image and the blurred estimate
        error = image / (blurred_estimate + 1e-10)

        # Update the deblurred image
        deblurred_image *= convolve2d(error, psf[::-1, ::-1], 'same', 'symm')

        # Update the PSF
        psf_update = convolve2d(image / (convolve2d(deblurred_image, psf, 'same', 'symm') + 1e-10),
                                deblurred_image[::-1, ::-1], 'full', 'symm')
        psf_update = psf_update[:psf_size[0], :psf_size[1]]
        psf += psf_update

        # Normalize the PSF to ensure it sums to 1
        psf /= np.sum(psf)

    return deblurred_image, psf