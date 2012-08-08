#!/usr/bin/env python
"""
====================================================
rosSensor.py - Sensor handler for the ROS interface
====================================================
"""

import roslib
import rospy
from sensor_msgs.msg import *

class rosSensorHandler:
	def __init__(self, proj, shared_data):
		"""
		ROS Sensor Handler
		"""
		self.rosInitHandler = shared_data['ROS_INIT_HANDLER']

	###################################
	### Available sensor functions: ###
	###################################

	def _subscriber(self, initial=False):
		"""
		This is a template for a subscriber type sensor interface
		"""
		def processData(data):
			# Do some processing here
			# Set the returnVal to either True or False based on the data
			self.returnVal = False
		if initial:
			# This is the topic you want to listen to
			self.topic = ''
			# This is the message type that the topic broadcasts
			# It is also the data type that gets passed to processData
			self.messageType = ''
		else:
			# There is already an initiated node for LTLMoP
			# This creates a subscriber for the given topic
			rospy.Subscriber(self.topic, self.messageType, processData)
			# You must return boolean
			return self.returnVal

	def tiltScan(self, operator='<', value=9.0, initial=False):
		"""
		This is a sample sensor interface utilizing the tilt_scan

		operator (str): How to compare the value to the data (default='<')
		value (float): The value to compare the data to in m (default=9.0)
		"""
		self.value=value
		def processData(data):
			try:
				avgRange=sum(data.ranges)/len(data.ranges)
			except:
				print 'No Range Data'
			self.returnVal = eval(str(avgRange)+operator+str(self.value))
		if initial:
			self.topic = 'tilt_scan'
			self.messageType = 'LaserScan'
		else:
			self.returnVal=False
			try:
				rospy.Subscriber(self.topic, eval(self.messageType), processData)
			except:
				print "Subscriber Failed"
			return self.returnVal

	def _service(self, initial=False):
		"""
		This is a template for a service type sensor interface
		"""
		def handleData(data):
			# Do some processing to the data here
			# Return a boolean based on the data
			return False
		if initial:
			# This is the name of the service you want to create
			self.serviceName=''
			# This is the message type for the service
			self.messageType=''
		else:
		# There is already an initiated node for LTLMoP
			# This creates the service
			response = rospy.Service(self.serviceName, self.messageType, handleData)
			return response
