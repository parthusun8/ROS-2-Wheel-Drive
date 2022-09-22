#!/usr/bin/env python

import rospy
from std_msgs.msg import String


def node_1():
	rospy.init_node('node1', anonymous = True) #Initialising Node
	pub = rospy.Publisher('Topic1', String, queue_size=10)
	rate = rospy.Rate(10)

	while not rospy.is_shutdown():
		publish_value = "subscribed to Topic1 successfully"
		pub.publish(publish_value)
		rate.sleep()

if __name__ == '__main__':
	try:
		node_1()
	except rospy.ROSInterruptException:
		pass