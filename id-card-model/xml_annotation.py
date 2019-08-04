import os #import os library
import cv2
from lxml import etree 	#import etree library from lxml folder
import xml.etree.cElementTree as et 	#importing cElementTree class from xml/etree.py as et.


def write_xml(folder, img, objects, tl, br, savedir):	#creating user-defined function write_xml with parameters as given tl=topleft and br=bottomright co-ordinates.
	if not os.path.isdir(savedir): 	#if given 'savedir' named folder is not present in current path.
		os.mkdir(savedir)	#make a directory/folder named 'savedir'  #'savedir' is parameter it may be any named.

	image = cv2.imread(img.path)	#read the image-path from current directory.
	height, width, depth = image.shape #geting the image size and putting their height width and depth in given variable height width and depth.

#we have to create xml file like that

# <annotation>	//root tag
#   <folder>image</folder>
#   <filename>0001.jpg</filename>
#   <segmented>0</segmented>
#   <size>
#     <width>4160</width>
#     <height>2340</height>
#     <depth>3</depth>
#   </size>

#   <object>
#     <name>AOT-ID-Card</name>
#     <pose>Unspecified</pose>
#     <truncated>0</truncated>
#     <bndbox>
#       <xmin>1254</xmin>
#       <ymin>711</ymin>
#       <xmax>2550</xmax>
#       <ymax>2257</ymax>
#     </bndbox>
#   </object>

#   <object>
#     <name>AOT-ID-Card</name>
#     <pose>Unspecified</pose>
#     <truncated>0</truncated>
#     <bndbox>
#       <xmin>1254</xmin>
#       <ymin>711</ymin>
#       <xmax>2550</xmax>
#       <ymax>2257</ymax>
#     </bndbox>
#   </object>
# </annotation>

	annotation = et.Element('annotation')	#creating first/root xml-tag named 'annotation'.
	et.SubElement(annotation,'folder').text = folder	#creating sub-xml-tag of named 'folder' under root xml-tag 'annotation' and putting the folder value.
	et.SubElement(annotation,'filename').text = img.name 	#similary created sub-xml tag named 'filename' and put img name by img.name
	et.SubElement(annotation,'segmented').text = '0'	#similary created 'segmented' and places the value '0'.

	size = et.SubElement(annotation,'size')	#now we create a subelement 'size' in annotation.
	et.SubElement(size,'width').text = str(width)	#now ,creating the width element in size tag and putting string value of width.
	et.SubElement(size,'height').text = str(height)	#similary for height and depth...
	et.SubElement(size,'depth').text = str(depth)

	for obj, topl, botr in zip(objects, tl, br):	#now for every selected object/s (may be one or more in one pics.), 
	#zip the objects, topleft and bottom right array. and for each array generate object tag in which write the info about objects i.e selected co-ordinates.
		ob = et.SubElement(annotation,'object')	#creation of sub-element in annotation tag, 'object' tag/element.
		et.SubElement(ob,'name').text = obj 	#now create name tag within 'object' tag and put the name of object.
		et.SubElement(ob,'pose').text = 'Unspecified' #similarly created 'pose' tag and value should be unspecified.
		et.SubElement(ob,'truncated').text = '0' #similarly truncated will be '0'.

		bbox = et.SubElement(ob,'bndbox') #now to put bounding boxes info in object create 'bbox' tag within object tag. 
		et.SubElement(bbox,'xmin').text = str(topl[0]) #within 'object' tag put x co-ordinate string value from topleft co-ordinate as'xmin' 
		et.SubElement(bbox,'ymin').text = str(topl[1]) #similarly 'ymin'.
		et.SubElement(bbox,'xmax').text = str(botr[0]) #similarly 'xmax' from bottomright co-ordinate.
		et.SubElement(bbox,'ymax').text = str(botr[1]) #similarly 'ymax'.

	xml_str = et.tostring(annotation) #converting info within root tag 'annotation' to string.
	root = etree.fromstring(xml_str)	#it formats the xml code means it put tabs when new sub tag is created within that tags.
	xml_str = etree.tostring(root, pretty_print = True) #create xml-tree structure as given xml-code above.

	save_path = os.path.join(savedir, img.name.replace('jpg','xml')) #it save the xml-annotation to a file name
	# as same name of image only extension has been changed to 'xml' in given 'annotation' folder.
	with open(save_path, 'wb') as temp_xml: #it append the file in given 'save_path' folder/directory. 
		temp_xml.write(xml_str)
