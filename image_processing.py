import cv2 #importing openCV package of version-2
import matplotlib.pyplot as plt #importing pyplot method/class from matplotlib package as plt.
from darkflow.net.build import TFNet #import TFNet method from darkflow/net/build.py
import numpy as np #import numpy as np


options={
	'model' : 'cfg/yolo.cfg',	#model path from current directory
	'load' : 'bin/yolov2.weights', # weights path from current directory #when we put '-1' at the place of 'path of weight' it takes latest trained model weight-path.
	'threshold' : 0.3,	#threshold value for create box around object.
	'gpu' : 1.0 #gpu version we can put here 0.0 - 1.0
}

colors=[255*np.random.rand(3) for i in range(10)] 	#for generating 10 random color in rgb(0 to 255,0 to 255,0 to 255).

tfnet=TFNet(options) #creating TFNet object by passing our model-option.

img = cv2.imread('sample_img/sample_dog.jpg', cv2.IMREAD_COLOR)  # read image in BGR color value, cv2.imread('path of image','read in color value')

results = tfnet.return_predict(img)  #it predict the image and generate values in the form of dictionary.. 
#	{'label':'value', 'confidence': 'value', topleft:co-ordinate, bottomright: co-ordinate}
#	you can check it by---> 'print(results)'
#Example->
#	{'label': 'AOT-ID-Card', 'confidence': 0.42267793, 'topleft': {'x': 970, 'y': 407}, 'bottomright': {'x': 2743, 'y': 1664}}
#	{'label': 'AOT-ID-Card', 'confidence': 0.41074792, 'topleft': {'x': 3336, 'y': 1021}, 'bottomright': {'x': 4104, 'y': 2038}} '''


for color,result in zip(colors,results): # zip(colors,results)-> it combines the colors and results together,it used for easy to access
	# color=colors[i], result=results[i]	, it takes value like that...

	tl = (result['topleft']['x'],result['topleft']['y']) #extract the 'top-left co-ordinates' of image in the form of tl = (x,y)
	br = (result['bottomright']['x'],result['bottomright']['y'])	#extract the 'bottom-right co-ordinates' of image in the form of br = (x,y)
	label = result['label']	#it extracts label. like 'AOT-ID-Card' from above
	confidence = result['confidence'] #it extract confidence value in float-value.

	label = "{} : {:0.2f}%".format(label,confidence*100) #we formatting the label by merging label and confidence in % upto 2 floating precision. 

	img = cv2.rectangle(img, tl, br, color, 8) #creating rectangle on detected object
	# by passing argument in 'cv2.rectangle('image-file','topleft co-ordinate','bottom-right co-ordinate', 'width of the line')'

	img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) #converting image-file into BGR to RGB color value

	img = cv2.putText(img, label,t1, cv2.FONT_HERSHEY_SIMPLEX, 2, color,8) #put label or name of object on top-left rectangle so, it specify object-name

plt.imshow(img) #image window pop and show the image.
plt.show()