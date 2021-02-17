#!/usr/bin/env python
import rospy
import sys
from stream.msg import *
from std_msgs.msg import *

def main(argv):
	rospy.init_node('clockNode', anonymous=True)
	pub = rospy.Publisher(name = 'stream_clock', data_class = Int64, latch = True, queue_size = 1000)
	rate = rospy.Rate(10)
	count = 0
	while not rospy.is_shutdown():
		pub.publish(count)
		count += 1
		rate.sleep()

if __name__ == '__main__':
	main(sys.argv)