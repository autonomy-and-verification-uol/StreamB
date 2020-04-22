#!/usr/bin/env python
import rospy
import sys
from sortedcontainers import SortedDict
from threading import *
from stream.msg import *
from std_msgs.msg import *

ws_lock = Lock()

dict_msgs = SortedDict()
def callbacka_(data):
	ws_lock.acquire()
	if data.time not in dict_msgs:
		dict_msgs[data.time] = set()
	dict_msgs[data.time].add(('l', data.value))
	conditional_publish()
	ws_lock.release()
def callbackb_(data):
	ws_lock.acquire()
	if data.time not in dict_msgs:
		dict_msgs[data.time] = set()
	dict_msgs[data.time].add(('r', data.value))
	conditional_publish()
	ws_lock.release()

attempts = 0
def conditional_publish():
	global attempts
	if len(dict_msgs.peekitem(0)[1]) == 2:
		e1 = dict_msgs.peekitem(0)[1].pop()
		e2 = dict_msgs.peekitem(0)[1].pop()
		msg = TimedBool()
		msg.time = dict_msgs.peekitem(0)[0]
		if e1[0] == 'l':
			msg.value = (e1[1]  -  e2[1])
		else:
			msg.value = (e2[1]  -  e1[1])
		pub.publish(msg)
		dict_msgs.popitem(0)
		attempts = 0
	elif attempts > 4:
		attempts = 0
		dict_msgs.popitem(0)
	else:
		attempts += 1

def main(argv):
	global pub, monitor
	rospy.init_node('two_stream_diff_monitor_0', anonymous=True)
	pub = rospy.Publisher(name = 'two_stream_diff_monitor_0', data_class = TimedReal, latch = True, queue_size = 1000)
	rospy.Subscriber('a_', TimedReal, callbacka_)
	rospy.Subscriber('b_', TimedInt, callbackb_)
	rospy.spin()

if __name__ == '__main__':
	main(sys.argv)