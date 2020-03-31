#!/usr/bin/env python
import rospy
import intervals
import sys
from threading import *
from stream.msg import *
from std_msgs.msg import *

def callback(data):
	pub.publish(data)
	print('velocity_turning_ok = ' + str(data.value))

def main(argv):
	global pub
	rospy.init_node('monitor_velocity_turning_ok', anonymous=True)
	rospy.Subscriber('mtl_monitor_18', TimedBool, callback)
	pub = rospy.Publisher(name = 'velocity_turning_ok', data_class = TimedBool, latch = True, queue_size = 1000)
	rospy.spin()
if __name__ == '__main__':
	main(sys.argv)