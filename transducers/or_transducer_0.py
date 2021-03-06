#!/usr/bin/env python
import rospy
import sys
from sortedcontainers import SortedDict
from threading import *
from stream.msg import *
from std_msgs.msg import *

ws_lock = Lock()

dict_msgs = SortedDict()
def callbackyellow(data):
	ws_lock.acquire()
	if data.time not in dict_msgs:
		dict_msgs[data.time] = set()
	dict_msgs[data.time].add(('l', data.value))
	conditional_publish()
	ws_lock.release()
def callbackorange(data):
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
			msg.value = (e1[1]  or  e2[1])
		else:
			msg.value = (e2[1]  or  e1[1])
		pub.publish(msg)
		dict_msgs.popitem(0)
		attempts = 0
	elif attempts > 4:
		attempts = 0
		dict_msgs.popitem(0)
	else:
		attempts += 1

def main(argv):
	global pub, transducer
	rospy.init_node('or_transducer_0', anonymous=True)
	pub = rospy.Publisher(name = 'or_transducer_0', data_class = TimedBool, latch = True, queue_size = 1000)
	rospy.Subscriber('yellow', TimedBool, callbackyellow)
	rospy.Subscriber('orange', TimedBool, callbackorange)
	rospy.spin()

if __name__ == '__main__':
	main(sys.argv)