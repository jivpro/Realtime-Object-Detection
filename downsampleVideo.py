import cv2
from darkflow.net.build import TFNet
import numpy as np
import time
import sys

option = {
    'model': 'cfg/yolo.cfg',
    'load': 'bin/yolov2.weights',
    'threshold': 0.1,
    'gpu': 1.0
}

tfnet=TFNet(option)
colors = [tuple(255*np.random.rand(3)) for i in range(10)]

capture = cv2.VideoCapture(sys.argv[1])
size = (
    int(capture.get(cv2.CAP_PROP_FRAME_WIDTH)),
    int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
)
codec = cv2.VideoWriter_fourcc(*'DIVX')
output = cv2.VideoWriter('videofile_1080_20fps.avi', codec, 60.0, size)

i = 0
frame_rate_divider = 3
while(capture.isOpened()):
    stime=time.time()
    ret, frame = capture.read()
    if ret:
        if i % frame_rate_divider == 0:
            # frame = cv2.resize(frame, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_CUBIC)
            results = tfnet.return_predict(frame)
            for color, result in zip(colors,results):
                t1 = (result['topleft']['x'], result['topleft']['y'])
                t2 = (result['bottomright']['x'], result['bottomright']['y'])
                label = result['label']
                confidence = result['confidence']

                text = '{} : {:0.0f}%'.format(label, confidence * 100)
                frame = cv2.rectangle(frame, t1, t2, color, 4)
                frame = cv2.putText(frame, text, t1, cv2.FONT_HERSHEY_COMPLEX,1, color, 2)
            output.write(frame)
            cv2.imshow('frame', frame)
            print('FPS {:.1f}'.format(1/(time.time()-stime)))
            i += 1
        else:
            i += 1
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

capture.release()
output.release()
cv2.destroyAllWindows()