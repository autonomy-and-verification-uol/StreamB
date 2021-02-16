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
		for i in range(0, 3):
			values.put(value)
	if time > lastTime:
		while (time - lastTime) > 1:
			values.put(lastValue)
			lastTime += 1
		values.put(value)
	while values.qsize() > 3:
		values.get()
	avg = 0
	for i in range(3):
		v = values.get()
		values.put(v)
		avg = avg + (v - avg) / (i + 1)
	if time > lastTime:
		lastValue = value
		lastTime += 1
	return avg
def callbackradiation_(data):
	ws_lock.acquire()
	msg = TimedReal()
	msg.time = data.time
	msg.value = aggregate(data.time, data.value)
	pub.publish(msg)
	ws_lock.release()
def main(argv):
	global pub, monitor
	rospy.init_node('tavg_monitor_2', anonymous=True)
	pub = rospy.Publisher(name = 'tavg_monitor_2', data_class = TimedReal, latch = True, queue_size = 1000)
	rospy.Subscriber('radiation_', TimedReal, callbackradiation_)
	rospy.spin()

if __name__ == '__main__':
	main(sys.argv)