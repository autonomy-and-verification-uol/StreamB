#!/usr/bin/env python
import rospy
import sys
from sortedcontainers import SortedDict
from threading import *
from stream.msg import *
from std_msgs.msg import *

ws_lock = Lock()

def callbacksoc_est_(data):
	ws_lock.acquire()
	msg = TimedBool()
	msg.time = data.time
	msg.value = data.value  >  0
	pub.publish(msg)
	ws_lock.release()


def main(argv):
	global pub, monitor
	rospy.init_node('greater_monitor_10', anonymous=True)
	pub = rospy.Publisher(name = 'greater_monitor_10', data_class = TimedBool, latch = True, queue_size = 1000)
	rospy.Subscriber('soc_est_', TimedReal, callbacksoc_est_)
	rospy.spin()

if __name__ == '__main__':
	main(sys.argv)