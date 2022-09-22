#!/usr/bin/env python

import rospy
from std_msgs.msg import String

def callback(value):
	rospy.loginfo("%s",value.data)

def bucket():
	rospy.init_node('node3', anonymous=True)

	rospy.Subscriber('Topic2', String, callback)

	rospy.spin()

if __name__ == '__main__':
	try:
		bucket()
	except rospy.ROSInterruptException:
		pass