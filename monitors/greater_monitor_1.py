#!/usr/bin/env python
import rospy
import sys
from sortedcontainers import SortedDict
from threading import *
from stream.msg import *
from std_msgs.msg import *

ws_lock = Lock()

def callbacktwo_stream_diff_monitor_0(data):
	ws_lock.acquire()
	msg = TimedBool()
	msg.time = data.time
	msg.value = data.value  >  0
	pub.publish(msg)
	ws_lock.release()


def main(argv):
	global pub, monitor
	rospy.init_node('greater_monitor_1', anonymous=True)
	pub = rospy.Publisher(name = 'greater_monitor_1', data_class = TimedBool, latch = True, queue_size = 1000)
	rospy.Subscriber('two_stream_diff_monitor_0', TimedReal, callbacktwo_stream_diff_monitor_0)
	rospy.spin()

if __name__ == '__main__':
	main(sys.argv)