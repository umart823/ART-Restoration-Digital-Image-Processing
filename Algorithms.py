import cv2
import bm3d
import numpy as np
import cv2
import os

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

