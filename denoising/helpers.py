import cv2
import numpy as np


def blur_and_threshold(image, eps=1e-7):
    # apply a median blur to the image and then subtract the blurred
    # image from the original image to approximate the foreground
    blur = cv2.medianBlur(image, 5)
    foreground = image.astype("float") - blur
    foreground[foreground > 0] = 0
    minVal = np.min(foreground)
    maxVal = np.max(foreground)
    foreground = (foreground - minVal) / (maxVal - minVal + eps)
    return foreground

