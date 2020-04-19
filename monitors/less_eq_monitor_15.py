#!/usr/bin/env python
import rospy
import sys
from sortedcontainers import SortedDict
from threading import *
from stream.msg import *
from std_msgs.msg import *

ws_lock = Lock()

def callbacktmax_monitor_14(data):
	ws_lock.acquire()
	msg = TimedBool()
	msg.time = data.time
	msg.value = data.value  <=  10
	print(str(data.value) + '  <=  ' + str(10) + '=' + str(msg.value))
	pub.publish(msg)
	ws_lock.release()


def main(argv):
	global pub, monitor
	rospy.init_node('less_eq_monitor_15', anonymous=True)
	pub = rospy.Publisher(name = 'less_eq_monitor_15', data_class = TimedBool, latch = True, queue_size = 1000)
	rospy.Subscriber('tmax_monitor_14', TimedReal, callbacktmax_monitor_14)
	rospy.spin()

if __name__ == '__main__':
	main(sys.argv)