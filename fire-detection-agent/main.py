import numpy as np
import cv2
import vision
import time
import http_request
import copy

class FireDetectionEngine :

	def __init__(self):
		self.envErrorRate = 0
		self.bufferRate = 0.5
		self.motionRate = 0.5

	def takeImage(self):
		cap = cv2.VideoCapture(0)
		if cap.isOpened():
			_, frame = cap.read()
		cap.release()
		return frame

	def showImage(self, image, caption):
		cv2.imshow(caption, image)
		cv2.waitKey(0)
	
	def initialize(self):
		initFrame = self.takeImage()
		self.envErrorRate = vision.pixelEstimate(initFrame)
		print(self.envErrorRate)
		self.showImage(initFrame, "Initial image")

	def imageDifference(self, image1, image2):
		vision.colorSegmentation(image1)
		vision.colorSegmentation(image2)
		result = np.absolute(image1 - image2)
		vision.colorSegmentation(result)
		return result
	
	def binaryDifference(self, img1, img2):
		grayImage1 = cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
		grayImage2 = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)

		ret1, thImg1 = cv2.threshold(grayImage1,127,255,cv2.THRESH_BINARY) 
		ret2, thImg2 = cv2.threshold(grayImage2,127,255,cv2.THRESH_BINARY)

		result = np.absolute(thImg2 - thImg1)
		return result


# Driver code for running the engine

fdEngine = FireDetectionEngine()

fdEngine.initialize()

while True : 
	time.sleep(2)
	image = fdEngine.takeImage()
	firePixelRate = vision.pixelEstimate(image)
	if firePixelRate - fdEngine.envErrorRate > fdEngine.bufferRate :
		time.sleep(2)
		image2 = fdEngine.takeImage()
		notificationCopyImage = copy.copy(image2)
		firePixelRateImg2 = vision.pixelEstimate(image2)
		if firePixelRateImg2 - fdEngine.envErrorRate > fdEngine.bufferRate:
			vision.colorSegmentation(image)
			vision.colorSegmentation(image2)
			imgDiff = fdEngine.binaryDifference(image, image2)
			motionRate = vision.binaryEstimate(imgDiff)
			if motionRate > fdEngine.motionRate + fdEngine.envErrorRate:
				print("Fire detected : ", firePixelRate - fdEngine.envErrorRate)
				fdEngine.showImage(image,"fire image")
				fdEngine.showImage(image2,"fire image")
				fdEngine.showImage(imgDiff,"fire image")
				print("Sending notification")
				if http_request.sendNotification("http://192.168.0.5:90/fdp/Api/FireAlert", notificationCopyImage, firePixelRateImg2, 0, 0) == "ok" :
					print("Successfully sent")
				else:
					print("sending notification failed")
			else:
				print("Static object")
		else:
			print("Spark")
	else:
		print("No fire : ", firePixelRate - fdEngine.envErrorRate)