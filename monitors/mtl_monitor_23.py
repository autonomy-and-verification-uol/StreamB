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

class mtl_monitor_23(BaseMonitor):

	time = -1
	states = [False, False, False, False, False, True]

	def update(self, **kwargs):

		self.time = self.time + 1
		self.states[0] = not(kwargs['is_turning']);
		self.states[1] = kwargs['less_eq_monitor_19'] and kwargs['less_eq_monitor_20'];
		self.states[2] = self.states[1] and kwargs['less_eq_monitor_21'];
		self.states[3] = self.states[2] and kwargs['less_eq_monitor_22'];
		self.states[4] = not self.states[0] or self.states[3];
		self.states[5] = self.states[5] and self.states[4];

		return self.states[5]

	def output(self):
		return self.states[5]


dict_msgs = SortedDict()
def callbackless_eq_monitor_22(data):
	ws_lock.acquire()
	if data.time not in dict_msgs:
		dict_msgs[data.time] = set()
	dict_msgs[data.time].add(('less_eq_monitor_22', data.value))
	conditional_publish()
	ws_lock.release()
def callbackis_turning(data):
	ws_lock.acquire()
	if data.time not in dict_msgs:
		dict_msgs[data.time] = set()
	dict_msgs[data.time].add(('is_turning', data.value))
	conditional_publish()
	ws_lock.release()
def callbackless_eq_monitor_20(data):
	ws_lock.acquire()
	if data.time not in dict_msgs:
		dict_msgs[data.time] = set()
	dict_msgs[data.time].add(('less_eq_monitor_20', data.value))
	conditional_publish()
	ws_lock.release()
def callbackless_eq_monitor_19(data):
	ws_lock.acquire()
	if data.time not in dict_msgs:
		dict_msgs[data.time] = set()
	dict_msgs[data.time].add(('less_eq_monitor_19', data.value))
	conditional_publish()
	ws_lock.release()
def callbackless_eq_monitor_21(data):
	ws_lock.acquire()
	if data.time not in dict_msgs:
		dict_msgs[data.time] = set()
	dict_msgs[data.time].add(('less_eq_monitor_21', data.value))
	conditional_publish()
	ws_lock.release()

attempts = 0
def conditional_publish():
	global attempts
	if len(dict_msgs.peekitem(0)[1]) == 5:
		kw = {}
		for (topic,value) in dict_msgs.peekitem(0)[1]:
			kw[topic] = value
		msg = TimedBool()
		msg.time = dict_msgs.peekitem(0)[0]
		msg.value = monitor.update(**kw)
		pub.publish(msg)
		dict_msgs.popitem(0)
		attempts = 0
	elif attempts > 10:
		attempts = 0
		dict_msgs.popitem(0)
	else:
		attempts += 1
def main(argv):
	global pub, monitor
	rospy.init_node('mtl_monitor_23', anonymous=True)
	monitor = mtl_monitor_23()
	rospy.Subscriber('less_eq_monitor_22', TimedBool, callbackless_eq_monitor_22)
	rospy.Subscriber('is_turning', TimedBool, callbackis_turning)
	rospy.Subscriber('less_eq_monitor_20', TimedBool, callbackless_eq_monitor_20)
	rospy.Subscriber('less_eq_monitor_19', TimedBool, callbackless_eq_monitor_19)
	rospy.Subscriber('less_eq_monitor_21', TimedBool, callbackless_eq_monitor_21)
	pub = rospy.Publisher(name = 'mtl_monitor_23', data_class = TimedBool, latch = True, queue_size = 1000)
	rospy.spin()
if __name__ == '__main__':
	main(sys.argv)