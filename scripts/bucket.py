#!/usr/bin/env python

import rospy
from std_msgs.msg import String

def callback(water):
	rospy.loginfo("%s",water.data)

def bucket():
	rospy.init_node('bucket', anonymous=True)

	rospy.Subscriber('Filling', String, callback)

	rospy.spin()

if __name__ == '__main__':
	try:
		bucket()
	except rospy.ROSInterruptException:
		pass