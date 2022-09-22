#!/usr/bin/env python

import rospy
from std_msgs.msg import String

def tap():
	rospy.init_node('tap', anonymous=True) #Initializing Node
	pub = rospy.Publisher('Filling', String, queue_size = 10)
	rate = rospy.Rate(10) #Hz

	water = 0

	while not rospy.is_shutdown():
		water += 0.5
		VideoPublish = "Water filled to " + str(water)
		if water == 100:
			rospy.loginfo("BUCKET IS COMPLETELY FILLED")
			break
		rospy.loginfo(VideoPublish)
		pub.publish(VideoPublish)
		rate.sleep()


if __name__ == '__main__':
	try:
		tap()
	except rospy.ROSInterruptException:
		pass