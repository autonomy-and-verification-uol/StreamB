#!/usr/bin/env python
import rospy
import sys
from threading import *
from stream.msg import *
from std_msgs.msg import *
from queue import *

ws_lock = Lock()

from queue import *
values = Queue()
lastTime = None
lastValue = None
def aggregate(time, value):
	global lastTime, lastValue
	if lastTime is None:
		lastTime = time - 1
		for i in range(0, 4):
			values.put(value)
	while (time - lastTime) > 1:
		values.put(lastValue)
		lastTime += 1
	values.put(value)
	while values.qsize() > 5:
		values.get()
	maximum = None
	for i in range(5):
		v = values.get()
		values.put(v)
		if maximum is None or v > maximum:
			maximum = v
	lastValue = value
	lastTime += 1
	return maximum
def callbackback_wheel_r_vel_(data):
	ws_lock.acquire()
	msg = TimedReal()
	msg.time = data.time
	msg.value = aggregate(data.time, data.value)
	pub.publish(msg)
	print('aggregate(' + str(data.value) + ') = ' + str(msg.value))
	ws_lock.release()
def main(argv):
	global pub, monitor
	rospy.init_node('tmax_monitor_12', anonymous=True)
	pub = rospy.Publisher(name = 'tmax_monitor_12', data_class = TimedReal, latch = True, queue_size = 1000)
	rospy.Subscriber('back_wheel_r_vel_', TimedReal, callbackback_wheel_r_vel_)
	rospy.spin()

if __name__ == '__main__':
	main(sys.argv)