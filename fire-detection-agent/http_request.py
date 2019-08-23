import requests
import json
import datetime
import cv2

def sendNotification(url, img, fireRate, smokeRate, temp):
    image = getImage(img)
    payload = {'FireRate':fireRate, 'SmokeRate':smokeRate, 'Temp':temp}
    fileName = "fireimage" + str(datetime.datetime.now().strftime("%Y-%m-%d-%H-%M")) + ".jpg"
    file = {'media' : (fileName,image)}
    response = requests.post(url, files=file, data=payload)
    return json.loads(response.text)['status']

def getImage(numpyArray):
    cv2.imwrite("temp.jpg", numpyArray)
    image = open("temp.jpg",'rb')
    return image
