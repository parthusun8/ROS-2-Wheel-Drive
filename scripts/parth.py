#!/usr/bin/env python

import rospy
from std_msgs.msg import String

def callback(video):
	rospy.loginfo("I watched the  ---  %s",video.data)

def parth():
	rospy.init_node('parth', anonymous=True)

	rospy.Subscriber('Pewdepie', String, callback)

	rospy.spin()

if __name__ == '__main__':
	try:
		parth()
	except rospy.ROSInterruptException:
		pass