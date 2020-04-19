#!/usr/bin/env python
import rospy
import intervals
import sys
from threading import *
from stream.msg import *
from std_msgs.msg import *
from sortedcontainers import *

ws_lock = Lock()

class BaseMonitor:
	def update_timed_since_inf(self, now, state, left, right, lower):
		if left and right:
			return (state & intervals.closed(self.time, intervals.inf)) | intervals.closed(self.time + lower, intervals.inf)
		elif not left and right:
			return intervals.closed(self.time + lower, intervals.inf)
		elif left and not right:
			return (state & intervals.closed(self.time, intervals.inf))
		else:
			return intervals.empty()
	def update_timed_since(self, now, state, left, right, lower, upper):
		if left and right:
			return (state & intervals.closed(self.time, intervals.inf)) | intervals.closed(self.time + lower, self.time + upper)
		elif not left and right:
			return intervals.closed(self.time + lower, self.time + upper)
		elif left and not right:
			return (state & intervals.closed(self.time, intervals.inf))
		else:
			return intervals.empty()
	def output_timed(self, state):
		return self.time in state

class mtl_monitor_4(BaseMonitor):

	time = -1
	states = [False, False, False]

	def update(self, **kwargs):

		self.time = self.time + 1
		self.states[0] = kwargs['neq_monitor_0'] or kwargs['neq_monitor_1'];
		self.states[1] = self.states[0] or kwargs['neq_monitor_2'];
		self.states[2] = self.states[1] or kwargs['neq_monitor_3'];

		return self.states[2]

	def output(self):
		return self.states[2]


dict_msgs = SortedDict()
def callbackneq_monitor_0(data):
	ws_lock.acquire()
	if data.time not in dict_msgs:
		dict_msgs[data.time] = set()
	dict_msgs[data.time].add(('neq_monitor_0', data.value))
	conditional_publish()
	ws_lock.release()
def callbackneq_monitor_1(data):
	ws_lock.acquire()
	if data.time not in dict_msgs:
		dict_msgs[data.time] = set()
	dict_msgs[data.time].add(('neq_monitor_1', data.value))
	conditional_publish()
	ws_lock.release()
def callbackneq_monitor_3(data):
	ws_lock.acquire()
	if data.time not in dict_msgs:
		dict_msgs[data.time] = set()
	dict_msgs[data.time].add(('neq_monitor_3', data.value))
	conditional_publish()
	ws_lock.release()
def callbackneq_monitor_2(data):
	ws_lock.acquire()
	if data.time not in dict_msgs:
		dict_msgs[data.time] = set()
	dict_msgs[data.time].add(('neq_monitor_2', data.value))
	conditional_publish()
	ws_lock.release()

attempts = 0
def conditional_publish():
	global attempts
	if len(dict_msgs.peekitem(0)[1]) == 4:
		kw = {}
		for (topic,value) in dict_msgs.peekitem(0)[1]:
			kw[topic] = value
		msg = TimedBool()
		msg.time = dict_msgs.peekitem(0)[0]
		msg.value = monitor.update(**kw)
		pub.publish(msg)
		dict_msgs.popitem(0)
		attempts = 0
	elif attempts > 8:
		attempts = 0
		dict_msgs.popitem(0)
	else:
		attempts += 1
def main(argv):
	global pub, monitor
	rospy.init_node('mtl_monitor_4', anonymous=True)
	monitor = mtl_monitor_4()
	rospy.Subscriber('neq_monitor_0', TimedBool, callbackneq_monitor_0)
	rospy.Subscriber('neq_monitor_1', TimedBool, callbackneq_monitor_1)
	rospy.Subscriber('neq_monitor_3', TimedBool, callbackneq_monitor_3)
	rospy.Subscriber('neq_monitor_2', TimedBool, callbackneq_monitor_2)
	pub = rospy.Publisher(name = 'mtl_monitor_4', data_class = TimedBool, latch = True, queue_size = 1000)
	rospy.spin()
if __name__ == '__main__':
	main(sys.argv)