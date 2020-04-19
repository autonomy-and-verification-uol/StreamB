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
		msg = TimedInt()
		msg.time = data.data
		msg.value = last
		pub.publish(msg)
	ws_lock.release()

def main(argv):
	global pub
	rospy.init_node('monitor_a2', anonymous=True)
	rospy.Subscriber('a2', Int64, callback)
	rospy.Subscriber('stream_clock', Int64, callbackClock)
	pub = rospy.Publisher(name = 'a2_', data_class = TimedInt, latch = True, queue_size = 1000)
	rospy.spin()
if __name__ == '__main__':
	main(sys.argv)