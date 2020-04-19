#!/usr/bin/env python
import rospy
import sys
from sortedcontainers import SortedDict
from threading import *
from stream.msg import *
from std_msgs.msg import *

ws_lock = Lock()

def callbackback_wheel_l_vel_(data):
	ws_lock.acquire()
	msg = TimedBool()
	msg.time = data.time
	msg.value = data.value  !=  0
	print(str(data.value) + '  !=  ' + str(0) + '=' + str(msg.value))
	pub.publish(msg)
	ws_lock.release()


def main(argv):
	global pub, monitor
	rospy.init_node('neq_monitor_5', anonymous=True)
	pub = rospy.Publisher(name = 'neq_monitor_5', data_class = TimedBool, latch = True, queue_size = 1000)
	rospy.Subscriber('back_wheel_l_vel_', TimedReal, callbackback_wheel_l_vel_)
	rospy.spin()

if __name__ == '__main__':
	main(sys.argv)