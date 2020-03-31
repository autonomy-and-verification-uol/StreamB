#!/usr/bin/env python
import rospy
import intervals
import sys
from threading import *
from stream.msg import *
from std_msgs.msg import *

def callback(data):
	pub.publish(data)
	print('velocity_ok = ' + str(data.value))

def main(argv):
	global pub
	rospy.init_node('monitor_velocity_ok', anonymous=True)
	rospy.Subscriber('and_monitor_24', TimedBool, callback)
	pub = rospy.Publisher(name = 'velocity_ok', data_class = TimedBool, latch = True, queue_size = 1000)
	rospy.spin()
if __name__ == '__main__':
	main(sys.argv)