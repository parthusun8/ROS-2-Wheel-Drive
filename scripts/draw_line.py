#!/usr/bin/env python

import rospy
from std_msgs.msg import String

#We will try to make a life of length 10 cm here

line_length = 0

def Eraser_callback(erase):
	global line_length
	if line_length > 10:
		line_length -= float(erase.data)
		rospy.loginfo('ERASING %f',line_length)

def Pencil_callback(Pencil):
	global line_length
	line_length += float(Pencil.data)
	rospy.loginfo('DRAWING %f',line_length)

def draw_line():
	rospy.init_node('draw_line', anonymous=True)
	
	rospy.Subscriber('Pencil', String, Pencil_callback)

	global line_length
	# rospy.Subscriber('Pen', String, Pen_callback)
	rospy.Subscriber('Eraser', String, Eraser_callback)
	if line_length == 10:
		rospy.loginfo('Line is 10 cm LONG NOW')

	# rospy.Subscriber('Compass', String, Compass_callback)
	if line_length <= 10:
		rospy.spin()




if __name__ == '__main__':
	try:
		draw_line()
	except rospy.ROSInterruptException:
		pass