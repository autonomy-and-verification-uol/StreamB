#!/usr/bin/env python
import rospy
import sys
from sortedcontainers import SortedDict
from threading import *
from stream.msg import *
from std_msgs.msg import *

ws_lock = Lock()

def callbacktmax_monitor_12(data):
	ws_lock.acquire()
	msg = TimedBool()
	msg.time = data.time
	msg.value = data.value  <=  15
	print(str(data.value) + '  <=  ' + str(15) + '=' + str(msg.value))
	pub.publish(msg)
	ws_lock.release()


def main(argv):
	global pub, monitor
	rospy.init_node('less_eq_monitor_22', anonymous=True)
	pub = rospy.Publisher(name = 'less_eq_monitor_22', data_class = TimedBool, latch = True, queue_size = 1000)
	rospy.Subscriber('tmax_monitor_12', TimedReal, callbacktmax_monitor_12)
	rospy.spin()

if __name__ == '__main__':
	main(sys.argv)