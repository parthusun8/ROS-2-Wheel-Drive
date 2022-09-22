#!/usr/bin/env python

import rospy
from std_msgs.msg import String



def Draw():

	rospy.init_node('Stationary', anonymous=True)

	eraser = rospy.Publisher('Eraser', String, queue_size = 10)
	Pen = rospy.Publisher('Pen', String, queue_size = 10)
	Pencil = rospy.Publisher('Pencil', String, queue_size = 10)
	# Compass = rospy.Publisher('Compass', String, queue_size = 10)

	rate = rospy.Rate(10) #Hz


	while not rospy.is_shutdown():
		eraser.publish(str(0.3))
		Pen.publish(str(0.4))
		Pencil.publish(str(0.4))
		# Compass.publish(str(0.3))
		rate.sleep()

if __name__ == '__main__':
	try:
		Draw()
	except rospy.ROSInterruptException:
		pass