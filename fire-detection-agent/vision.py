import cv2
import numpy as np


def colorSegmentation(image):
    try:
        conditionOne = image[: , : , 2] >= 200
        conditionTwo = image[:, : , 2] > image[:, : , 1]
        conditionThree = image[:, : , 1] > image[:, : , 0]

        result = np.logical_and(np.logical_and(conditionOne, conditionTwo), conditionThree)

        image[result[:, : ] == False] = (0, 0, 0)
        return image
    except Exception:
        print("Exception occured: possible reason - image not found")


def colorSegmentationAdvanced(image):
    try:
        conditionOne = image[: , : , 2] >= 200
        conditionTwo = image[:, : , 2] > image[:, : , 1]
        conditionThree = image[:, : , 1] > image[:, : , 0]
        conditionFour = image[:, :, 0] < 120

        #result = np.logical_and(np.logical_and(conditionOne, conditionTwo), conditionThree)
        res1 = np.logical_and(conditionOne, conditionTwo)
        res2 = np.logical_and(conditionThree, conditionFour)
        result = np.logical_and(res1, res2)
        image[result[:, :] == False] = (0, 0, 0)
        return image
    except Exception:
        print("Exception occured: possible reason - image not found")

def pixelEstimate(image):
    try:
        rows, cols, _ = image.shape
        counter = 0
        conditionOne = image[: , : , 2] >= 200
        conditionTwo = image[:, : , 2] > image[:, : , 1]
        conditionThree = image[:, : , 1] > image[:, : , 0]

        result = np.logical_and(np.logical_and(conditionOne, conditionTwo), conditionThree)
        counter = np.count_nonzero(result)
        percentage = (counter/(rows*cols)) * 100
        return percentage
    except Exception:
        print("Exception occured: possible reason - image not found")


def pixelEstimateAdvanced(image):
    try:
        rows, cols, _ = image.shape
        counter = 0
        conditionOne = image[: , : , 2] >= 200
        conditionTwo = image[:, : , 2] > image[:, : , 1]
        conditionThree = image[:, : , 1] > image[:, : , 0]
        conditionFour = image[:, :, 0] < 120

        #result = np.logical_and(np.logical_and(conditionOne, conditionTwo), conditionThree)
        res1 = np.logical_and(conditionOne, conditionTwo)
        res2 = np.logical_and(conditionThree, conditionFour)
        result = np.logical_and(res1, res2)
        counter = np.count_nonzero(result)
        percentage = (counter/(rows*cols)) * 100
        return percentage
    except Exception:
        print("Exception occured: possible reason - image not found")

def binaryEstimate(image):
    rows, cols = image.shape
    counter = np.count_nonzero(image)
    percentage = (counter/(rows*cols)) * 100
    return percentage