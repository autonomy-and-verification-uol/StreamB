#!/usr/bin/env python
import rospy
import intervals
import sys
from threading import *
from stream.msg import *
from std_msgs.msg import *

def callback(data):
	pub.publish(data)
	print('a = ' + str(data.value))

def main(argv):
	global pub
	rospy.init_node('monitor_a', anonymous=True)
	rospy.Subscriber('and_monitor_2', TimedBool, callback)
	pub = rospy.Publisher(name = 'a', data_class = TimedBool, latch = True, queue_size = 1000)
	rospy.spin()
if __name__ == '__main__':
	main(sys.argv)