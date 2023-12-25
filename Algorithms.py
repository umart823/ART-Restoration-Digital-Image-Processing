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

def CLAHE(imgPath,clipLimit=5.0,GridSize=10):
    image = cv2.imread(imgPath)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    clahe = cv2.createCLAHE(clipLimit, tileGridSize=(GridSize, GridSize))
    enhanced_image = clahe.apply(gray_image)
    return enhanced_image

# def Richardson_lucy_blind_deconvolution_psf(imgPath, num_iterations=10, psf_size=5):

# def Richardson_Lucy(imgPath, iterations, kernel_size):

def Automated_Crack_Fixing(imgPath, minEdgeRange, maxEdgeRange, minDesiredLineLength,maxDesiredLineLength,maxLineGap, KernelSize,KernelSize2):
    o_image=cv2.imraed(imgPath)
    image = cv2.cvtColor(o_image, cv2.COLOR_BGR2GRAY)
    image = image.astype("uint8")
    edges = cv2.Canny(image, minEdgeRange, maxEdgeRange)

    # Dilate the edges using a kernel (adjust the kernel size as needed)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (KernelSize, KernelSize))
    dilated_edges = cv2.dilate(edges, kernel)
    # cv2_imshow(dilated_edges)

    # Detect lines using HoughLinesP
    lines = cv2.HoughLinesP(dilated_edges, 1, np.pi/180, threshold=50, minLineLength=minDesiredLineLength, maxLineGap=maxLineGap)

    # Check if lines are detected

    filtered_lines = []
    if lines is not None:
      for line in lines:
          x1, y1, x2, y2 = line[0]
          if np.linalg.norm(np.array([x1, y1]) - np.array([x2, y2])) < maxDesiredLineLength:
              filtered_lines.append(line[0])
        # Draw lines on the original image
      output_image = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
      mask = np.zeros_like(output_image)
      for line in filtered_lines:
        x1, y1, x2, y2 = line
        cv2.line(output_image, (x1, y1), (x2, y2), (0, 0, 255), 2)
        cv2.line(mask, (x1, y1), (x2, y2), 255, 2)

      # cv2_imshow(output_image)

      mask = cv2.cvtColor(mask, cv2.COLOR_BGR2GRAY)
      _, mask = cv2.threshold(mask, 1, 255, cv2.THRESH_BINARY)

      kernel2 = cv2.getStructuringElement(cv2.MORPH_RECT, (KernelSize2, KernelSize2))
      mask = cv2.dilate(mask, kernel2)
      # cv2_imshow(mask)
      inpainting_method = cv2.INPAINT_TELEA  # Use the correct flag
      inpainted_image = cv2.inpaint(image, mask, inpainting_method, flags=cv2.INPAINT_TELEA)

    #   cv2_imshow(inpainted_image)
      return inpainted_image
    else:
        print("Sorry, No lines detected")

