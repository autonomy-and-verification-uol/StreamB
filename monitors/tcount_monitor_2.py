#!/usr/bin/env python
import rospy
import sys
from threading import *
from stream.msg import *
from std_msgs.msg import *
from queue import *
import math

ws_lock = Lock()

from queue import *
values = Queue()
lastTime = None
lastValue = None
def aggregate(time, value):
	global lastTime, lastValue
	if lastTime is None:
		lastTime = time - 1
		for i in range(0, 5):
			values.put(value)
	while (time - lastTime) > 1:
		values.put(lastValue)
		lastTime += 1
	values.put(value)
	while values.qsize() > 5:
		values.get()
	count = 0
	for i in range(5):
		v = values.get()
		values.put(v)
		if v:
			count = count + 1
	lastValue = value
	lastTime += 1
	return count
def callbackgreater_monitor_1(data):
	ws_lock.acquire()
	msg = TimedBool()
	msg.time = data.time
	msg.value = aggregate(data.time, data.value)
	pub.publish(msg)
	ws_lock.release()
def main(argv):
	global pub, monitor
	rospy.init_node('tcount_monitor_2', anonymous=True)
	pub = rospy.Publisher(name = 'tcount_monitor_2', data_class = TimedBool, latch = True, queue_size = 1000)
	rospy.Subscriber('greater_monitor_1', TimedBool, callbackgreater_monitor_1)
	rospy.spin()

if __name__ == '__main__':
	main(sys.argv)