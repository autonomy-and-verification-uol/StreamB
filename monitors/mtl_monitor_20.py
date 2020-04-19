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

class mtl_monitor_20(BaseMonitor):

	time = -1
	states = [False, False, False, False, True]

	def update(self, **kwargs):

		self.time = self.time + 1
		self.states[0] = kwargs['less_eq_monitor_11'] and kwargs['less_eq_monitor_13'];
		self.states[1] = self.states[0] and kwargs['less_eq_monitor_15'];
		self.states[2] = self.states[1] and kwargs['less_eq_monitor_17'];
		self.states[3] = not kwargs['is_turning'] or kwargs['mtl_monitor_18'];
		self.states[4] = self.states[4] and kwargs['mtl_monitor_19'];

		return self.states[4]

	def output(self):
		return self.states[4]


dict_msgs = SortedDict()
def callbackless_eq_monitor_17(data):
	ws_lock.acquire()
	if data.time not in dict_msgs:
		dict_msgs[data.time] = set()
	dict_msgs[data.time].add(('less_eq_monitor_17', data.value))
	conditional_publish()
	ws_lock.release()
def callbackmtl_monitor_19(data):
	ws_lock.acquire()
	if data.time not in dict_msgs:
		dict_msgs[data.time] = set()
	dict_msgs[data.time].add(('mtl_monitor_19', data.value))
	conditional_publish()
	ws_lock.release()
def callbackless_eq_monitor_11(data):
	ws_lock.acquire()
	if data.time not in dict_msgs:
		dict_msgs[data.time] = set()
	dict_msgs[data.time].add(('less_eq_monitor_11', data.value))
	conditional_publish()
	ws_lock.release()
def callbackless_eq_monitor_15(data):
	ws_lock.acquire()
	if data.time not in dict_msgs:
		dict_msgs[data.time] = set()
	dict_msgs[data.time].add(('less_eq_monitor_15', data.value))
	conditional_publish()
	ws_lock.release()
def callbackless_eq_monitor_13(data):
	ws_lock.acquire()
	if data.time not in dict_msgs:
		dict_msgs[data.time] = set()
	dict_msgs[data.time].add(('less_eq_monitor_13', data.value))
	conditional_publish()
	ws_lock.release()
def callbackis_turning(data):
	ws_lock.acquire()
	if data.time not in dict_msgs:
		dict_msgs[data.time] = set()
	dict_msgs[data.time].add(('is_turning', data.value))
	conditional_publish()
	ws_lock.release()
def callbackmtl_monitor_18(data):
	ws_lock.acquire()
	if data.time not in dict_msgs:
		dict_msgs[data.time] = set()
	dict_msgs[data.time].add(('mtl_monitor_18', data.value))
	conditional_publish()
	ws_lock.release()

attempts = 0
def conditional_publish():
	global attempts
	if len(dict_msgs.peekitem(0)[1]) == 7:
		kw = {}
		for (topic,value) in dict_msgs.peekitem(0)[1]:
			kw[topic] = value
		msg = TimedBool()
		msg.time = dict_msgs.peekitem(0)[0]
		msg.value = monitor.update(**kw)
		pub.publish(msg)
		dict_msgs.popitem(0)
		attempts = 0
	elif attempts > 14:
		attempts = 0
		dict_msgs.popitem(0)
	else:
		attempts += 1
def main(argv):
	global pub, monitor
	rospy.init_node('mtl_monitor_20', anonymous=True)
	monitor = mtl_monitor_20()
	rospy.Subscriber('less_eq_monitor_17', TimedBool, callbackless_eq_monitor_17)
	rospy.Subscriber('mtl_monitor_19', TimedBool, callbackmtl_monitor_19)
	rospy.Subscriber('less_eq_monitor_11', TimedBool, callbackless_eq_monitor_11)
	rospy.Subscriber('less_eq_monitor_15', TimedBool, callbackless_eq_monitor_15)
	rospy.Subscriber('less_eq_monitor_13', TimedBool, callbackless_eq_monitor_13)
	rospy.Subscriber('is_turning', TimedBool, callbackis_turning)
	rospy.Subscriber('mtl_monitor_18', TimedBool, callbackmtl_monitor_18)
	pub = rospy.Publisher(name = 'mtl_monitor_20', data_class = TimedBool, latch = True, queue_size = 1000)
	rospy.spin()
if __name__ == '__main__':
	main(sys.argv)