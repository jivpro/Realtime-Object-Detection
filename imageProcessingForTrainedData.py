import cv2
import matplotlib.pyplot as plt
from darkflow.net.build import TFNet
import sys
import numpy as np


options={
	'model' : 'cfg/tiny-yolo-id-card.cfg',
	'load' : -1,
	'threshold' : 0.3,
	'gpu' : 1.0
}

colors=[255*np.random.rand(3) for i in range(10)]

tfnet=TFNet(options)
img = cv2.imread('id-card-model/image/0372.jpg', cv2.IMREAD_COLOR)
results = tfnet.return_predict(img)

for color,result in zip(colors,results):
	print(result)

	t1=(result['topleft']['x'],result['topleft']['y'])
	t2=(result['bottomright']['x'],result['bottomright']['y'])
	label = result['label']
	confidence = result['confidence']

	label = "{} : {:0.2f}%".format(label,confidence*100) 

	img = cv2.rectangle(img,t1,t2,color,8)
	img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
	img = cv2.putText(img, label,t1, cv2.FONT_HERSHEY_SIMPLEX, 2, color,8)

plt.imshow(img)
plt.show()