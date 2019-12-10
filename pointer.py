import numpy as np
import cv2
import os
import sys
from Xlib import X, display


def getcentroid(x, y, w, h):
	x = x + w / 2
	y = y + h / 2
	return(x, y)
	
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

cam = cv2.VideoCapture(0)
d = display.Display()
s = d.screen()
root = s.root

while True:
	
	_ , img = cam.read()
	img = cv2.flip(img, 1)
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	# print(gray.shape)
	# palms = palm_cascade.detectMultiScale(gray, 1.3, 5)
	faces = face_cascade.detectMultiScale(gray, 1.3, 5)
	for (x, y,w, h) in faces:
			cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
			points = getcentroid(x, y, w, h)
			p_x = (points[0] - 0) / (640 - 0) * 1920
			p_y = (points[1] - 0) / (480 - 0) * 1080
			root.warp_pointer(int(p_x), int(p_y))
			d.sync()
	cv2.imshow('img',img)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
	
cv2.destroyAllWindows()
