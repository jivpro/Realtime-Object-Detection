import os 	#importing os library.
import matplotlib.pyplot as plt #importing pyplot class from matplotlib library as plt.
import cv2 #importing openCV
from matplotlib.widgets import RectangleSelector #importing RectangleSelector method from matplotlib.widget.
from xml_annotation import write_xml #importing our own created method write_xml from xml_annotation.py file.



#creating global constants/variable
img = None 
tl_list = [] #craetion of empty topleft list.
br_list = [] #similarly bottom right list.
object_list = [] #similarly object list.

#constants
image_folder = 'image' #we are taking the images from 'image' folder. so, I have putted image_folder value is 'image'
savedir = 'annotation' #We will save the 'xml' annotation file in 'annotation' folder.So, I have putted savedir value is'annotation
obj = 'AOT-ID-Card' #Now object name should be 'AOT-ID-Card'. So, I have putted obj value to 'AOT-ID-Card'.

def lineSelect_CallBack(clk,rls): #define a function which takes click(clk)(i.e from where we start the image selection) value and release(rls) value where we stop selection.
	global tl_list
	global br_list
	global object_list
	tl_list.append((int(clk.xdata),int(clk.ydata))) #append the integer value of 'x' & 'y' co-ordinate of click(clk) co-ordinate as top-left list.
	br_list.append((int(rls.xdata),int(rls.ydata))) #similary appends release(rls) co-ordinates integer value to bottomright list.
	object_list.append(obj) #append the object name to object_list.

def onKeyPress(event): #creation of key-press event means when we press a key from key board then what action will done.
	global tl_list
	global br_list
	global object_list
	global img

	if event.key == 'q': #when we press 'q' from key-board.
		# print('{} : {}'.format(object_list, img)) #these two lines are not neccessary it just for checking purpose.
		# print(tl_list,br_list)
		
		write_xml(image_folder, img, object_list, tl_list, br_list, savedir) #passing all parameters to our created method 'write_xml'
		#which is we have imported from annotation.py file.
		
		tl_list = [] #now empty the all parameters.
		br_list = []
		object_list = []
		img = None
		plt.close() #image windows close 
#these all above action done when we press 'q'.

def toggle_selector(event): #for multiple object selection.
	toggle_selector.RS.set_active(True)


if __name__ == '__main__': #start execution your code from here...
	for n, image_file in enumerate(os.scandir(image_folder)): #for each image_file in 'image_folder' folder.
		img = image_file #putting img value to image_file.
		fig, ax = plt.subplots(1) #plot the image with horizontal & vertcal graphical bar value in left side and bottom side.
		mngr = plt.get_current_fig_manager() #craeting the figure manager object.
		mngr.window.setGeometry(30,30,1024,640) #resize your figure manager windows within these given co-cordinates (x1,y1) and (x2,y2).

		image = cv2.imread(image_file.path) #read the image from given pathwith color value BGR.
		image = cv2.cvtColor(image,cv2.COLOR_BGR2RGB) #now convert image to BGR to RGB color-value.
		ax.imshow(image) #show images in matplotlib-image-window.

		#for rectangular selection: rectangular selection will be line selection and these condition are neccessary you can change their value.
		toggle_selector.RS = RectangleSelector(
			ax, lineSelect_CallBack,
			drawtype = 'box', useblit = True,
			button = [1], minspanx = 5, minspany = 5,
			spancoords = 'pixels', interactive = True
		)	

		bbox = plt.connect('key_press_event',toggle_selector) #calling the above key-press event methods.
		key = plt.connect('key_press_event', onKeyPress)	#calling the above key-press event methods.
		plt.tight_layout() 
		plt.show()
		plt.close(fig) #close the image window.