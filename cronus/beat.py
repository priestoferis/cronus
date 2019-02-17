"""
Implements the beat library

Date created: 19th May 2014
"""

import datetime
import time




class Beat():
	def __init__(self):
		self.loop_start_time = None
		self.loop_duration = 0

	def set_rate(self,rate):
		"""Defines the ideal rate at which computation is to be performed

		:arg rate: the frequency in Hertz 
		:type rate: int or float

		:raises: TypeError: if argument 'rate' is not int or float
		"""
		if not (isinstance(rate, int) or isinstance(rate, float)):
			raise TypeError("argument to set_rate is expected to be int or float")

		self.loop_duration = 1.0/rate

	def sleep(self):
		"""Sleeps for a dynamic duration of time as determined by set_rate() and true().
		
		:raises: BeatError: if this function is called before calling set_rate() or \
				before calling true()
		"""
		if self.loop_duration == 0:
			raise BeatError("call beat.set_rate() before calling sleep")
		if self.loop_start_time == None:
			raise BeatError("call beat.true() before calling sleep")
		td = datetime.datetime.now() - self.loop_start_time
		duration_to_sleep = self.loop_duration - td.total_seconds()
		if duration_to_sleep < 0:
			raise BeatError("skipping sleep. Too much work!")
		time.sleep(duration_to_sleep)

	def true(self):
		"""A substitute to True. Use 'while beat.true()' instead of 'while True'
		
		:returns: True
		"""

		self.loop_start_time = datetime.datetime.now()
		return True


class BeatError(Exception):

    def __init__(self, msg):
        self.msg = msg
        pass

    def __str__(self):
        return self.msg
