#!/usr/bin/env python
import rospy
import intervals
import sys
from threading import *
from stream.msg import *
from std_msgs.msg import *

ws_lock = Lock()
last = None
def callback(data):
	global last
	ws_lock.acquire()
	last = data.data
	ws_lock.release()
def callbackClock(data):
	ws_lock.acquire()
	if last is not None: 
		msg = TimedReal()
		msg.time = data.data
		msg.value = last
		pub.publish(msg)
	ws_lock.release()

def main(argv):
	global pub
	rospy.init_node('monitor_front_wheel_r_vel', anonymous=True)
	rospy.Subscriber('front_wheel_r_vel', Float64, callback)
	rospy.Subscriber('stream_clock', Int64, callbackClock)
	pub = rospy.Publisher(name = 'front_wheel_r_vel_', data_class = TimedReal, latch = True, queue_size = 1000)
	rospy.spin()
if __name__ == '__main__':
	main(sys.argv)