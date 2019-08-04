import cv2
from darkflow.net.build import TFNet
import numpy as np
import time

option = {
	'model': 'cfg/yolo.cfg',
	'load': 'bin/yolov2.weights',
	'threshold': 0.1,
	'gpu': 1.0
}

tfnet = TFNet(option)

colors = [tuple(255 * np.random.rand(3)) for i in range(10)]

capture = cv2.VideoCapture(0)	#at the place of video path, we simply put 0 to live processing from laptop webcam.
#below 2 lines is not neccessary...
capture.set(cv2.CAP_PROP_FRAME_WIDTH,1080)	#We set the our captured frame width to 1080p.
capture.set(cv2.CAP_PROP_FRAME_HEIGHT,720)	#We set the our captured frame height to 720p.
#all the remaining code is similar to video-processing.
while (capture.isOpened()):
	stime=time.time()
	ret, frame = capture.read()
	results = tfnet.return_predict(frame)

	if ret:
		for color, result in zip(colors,results):
			t1 = (result['topleft']['x'], result['topleft']['y'])
			t2 = (result['bottomright']['x'], result['bottomright']['y'])
			label = result['label']
			confidence = result['confidence']

			text = '{} : {:0.0f}%'.format(label, confidence * 100)
			frame = cv2.rectangle(frame, t1, t2, color, 4)
			frame = cv2.putText(frame, text, t1, cv2.FONT_HERSHEY_COMPLEX,1, color, 2)
		cv2.imshow('frame', frame)
		print('FPS : {:0.1f}'.format(1/(time.time()-stime)))
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

capture.release()
cv2.destroyAllWindows()
