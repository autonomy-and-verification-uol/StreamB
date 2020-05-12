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

class mtl_monitor_11(BaseMonitor):

	time = -1
	states = [True]

	def update(self, **kwargs):

		self.time = self.time + 1
		self.states[0] = self.states[0] and kwargs['greater_monitor_10'];

		return self.states[0]

	def output(self):
		return self.states[0]


dict_msgs = SortedDict()
def callbackgreater_monitor_10(data):
	ws_lock.acquire()
	if data.time not in dict_msgs:
		dict_msgs[data.time] = set()
	dict_msgs[data.time].add(('greater_monitor_10', data.value))
	conditional_publish()
	ws_lock.release()

attempts = 0
def conditional_publish():
	global attempts
	if len(dict_msgs.peekitem(0)[1]) == 1:
		kw = {}
		for (topic,value) in dict_msgs.peekitem(0)[1]:
			kw[topic] = value
		msg = TimedBool()
		msg.time = dict_msgs.peekitem(0)[0]
		msg.value = monitor.update(**kw)
		pub.publish(msg)
		dict_msgs.popitem(0)
		attempts = 0
	elif attempts > 2:
		attempts = 0
		dict_msgs.popitem(0)
	else:
		attempts += 1
def main(argv):
	global pub, monitor
	rospy.init_node('mtl_monitor_11', anonymous=True)
	monitor = mtl_monitor_11()
	rospy.Subscriber('greater_monitor_10', TimedBool, callbackgreater_monitor_10)
	pub = rospy.Publisher(name = 'mtl_monitor_11', data_class = TimedBool, latch = True, queue_size = 1000)
	rospy.spin()
if __name__ == '__main__':
	main(sys.argv)