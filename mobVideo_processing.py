import requests
import cv2
import numpy as np 
from darkflow.net.build import TFNet
import sys


options = {
	'model': 'cfg/tiny-yolo-id-card.cfg',
	'load': -1,
	'threshold': 0.3,
	'gpu': 1.0
}

tfnet = TFNet(options)

colors = [255*np.random.rand(3) for i in range(10)]

url="http://192.168.43.139:8080/shot.jpg"	#It takes the shots.jpg image every time (depends on frame rate-FPS).

while True:
	img_req = requests.get(url) #it gets the requests and read the frame shot.jpg every time.
	img_arr = np.array(bytearray(img_req.content), dtype = np.uint8)	#it first converts img_req contents to byte-array and then 
	#be put it into numpy array of data type np.uint8.
	
	frame = cv2.imdecode(img_arr, 1)	#decode the numpy image-array to color-code values.

	#all the remaining codes are similar to others video processing codes.....
	results = tfnet.return_predict(frame)
	
	for color,result in zip(colors,results):
		top_left = (result['topleft']['x'], result['topleft']['y'])
		bottom_right = (result['bottomright']['x'], result['bottomright']['y'])
		label = result['label']
		confidence = result['confidence']

		label = "{} : {}%".format(label,confidence*100)

		frame = cv2.rectangle(frame, top_left, bottom_right, color, 2)
		frame = cv2.putText(frame, label, top_left, cv2.FONT_HERSHEY_COMPLEX, 1, color, 2)

	cv2.imshow("AndroidCam",frame)

	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

cv2.destroyAllWindows()