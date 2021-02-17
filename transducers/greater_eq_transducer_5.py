#!/usr/bin/env python
import rospy
import sys
from sortedcontainers import SortedDict
from threading import *
from stream.msg import *
from std_msgs.msg import *

ws_lock = Lock()

def callbacktavg_transducer_2(data):
	ws_lock.acquire()
	msg = TimedBool()
	msg.time = data.time
	msg.value = data.value  >=  120
	pub.publish(msg)
	ws_lock.release()


def main(argv):
	global pub, transducer
	rospy.init_node('greater_eq_transducer_5', anonymous=True)
	pub = rospy.Publisher(name = 'greater_eq_transducer_5', data_class = TimedBool, latch = True, queue_size = 1000)
	rospy.Subscriber('tavg_transducer_2', TimedReal, callbacktavg_transducer_2)
	rospy.spin()

if __name__ == '__main__':
	main(sys.argv)