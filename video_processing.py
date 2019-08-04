import cv2
from darkflow.net.build import TFNet
import numpy as np
import time
import sys

option = {
    'model': 'cfg/tiny-yolo-id-card.cfg',
    'load': -1, #load latest checkpointing weights...
    'threshold': 0.6,
    'gpu': 1.0
}

tfnet = TFNet(option)

capture = cv2.VideoCapture('aot-id-card.mp4')	#reading the video from current directory, in which that .py file is present.
color = [tuple(255 * np.random.rand(3)) for i in range(5)]

while(capture.isOpened()):	#capture is opened 
    stime=time.time() #calculating the frame reading time.
    ret, frame = capture.read() #A frame is read from capture. ret holds frame read or not if read then ret=True else ret=False
    result = tfnet.return_predict(frame) #predict the frame 
    if ret: #if ret=True
    #all below is same as image processing...
        for colr,reslt in zip(color, result):
            t1 = (reslt['topleft']['x'], reslt['topleft']['y'])
            t2 = (reslt['bottomright']['x'], reslt['bottomright']['y'])

            label = reslt['label']
            confidence = reslt['confidence']

            label = '{} : {:0.2f}%'.format(label,confidence*100)
            
            frame = cv2.rectangle(frame, t1, t2, colr, 3)
            frame = cv2.putText(frame, label, t1, cv2.FONT_HERSHEY_COMPLEX, 1, colr, 2)
        cv2.imshow('frame',frame)
        print('FPS {:.1f}'.format(1/(time.time()-stime)))	#printing FPS rate of frame processing on terminal.

        if cv2.waitKey(1) & 0xFF == ord('q'):	#if you press 'q' key from keyboard it breaks the loop.
            break

capture.release()	#capture is released.
cv2.destroyAllWindows()	#all the open windows and resources due to this processing is destroy and closed.