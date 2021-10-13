import numpy as np
from random import random


class Channel():
	def __init__(self, dhndl_prob=1):
		'''
			dhndl_prob: float
				Dont handle probability.
				The probability that the requests will not be handled 

		'''
		self.__dhndl_prob = dhndl_prob
		self.__current_request = None

	@property
	def is_free(self):
		return not bool(self.__current_request)
	
	def put_request(self, request):
		if not self.__current_request:
			self.__current_request = request
			return True
		else:
			return False

	def tact(self):
		if self.__current_request:
			self.__current_request.inc_tacts()
			rand_num = random()
			if rand_num <= self.__dhndl_prob:
				return None
			else:
				request = self.__current_request
				self.__current_request = None
				return request

