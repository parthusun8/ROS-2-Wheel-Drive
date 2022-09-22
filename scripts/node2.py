#!/usr/bin/env python

import rospy
from std_msgs.msg import String

Topic_1_value = ""

def topic1_callback(value):
	global Topic_1_value
	Topic_1_value = value.data

def node_2():
	rospy.init_node('node2', anonymous=True)
	rospy.Subscriber('Topic1', String, topic1_callback)
	pub = rospy.Publisher('Topic2', String, queue_size=10)
	rate = rospy.Rate(10)

	while not rospy.is_shutdown():
		publish_value = "U Have subscribed to Topic2 successfully which is " + Topic_1_value
		pub.publish(publish_value)
		# rospy.loginfo("%s",publish_value)
		rate.sleep()


if __name__ == '__main__':
	try:
		node_2()
	except rospy.ROSInterruptException:
		pass
#sub to 1
#pub to 2