#!/usr/bin/env python

import rospy
from std_msgs.msg import String

def felix():
	rospy.init_node('felix', anonymous=True) #Initializing Node
	pub = rospy.Publisher('Pewdepie', String, queue_size = 10)
	rate = rospy.Rate(10) #Hz


	while not rospy.is_shutdown():
		VideoPublish = "Published New Video"
		rospy.loginfo(VideoPublish)
		pub.publish(VideoPublish)
		rate.sleep()


if __name__ == '__main__':
	try:
		felix()
	except rospy.ROSInterruptException:
		pass