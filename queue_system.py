from source import Source
from queue import Queue
from channel import Channel


class QueueSystem():
	def __init__(self, pi1, pi2):
		self.__source = self.__init_source(2)
		self.__queue = self.__init_queue(2)
		self.__channel_1 = self.__get_channel(pi1)
		self.__channel_2 = self.__get_channel(pi2)

		self.__system = (self.__source, self.__queue, self.__channel_1, self.__channel_2)

		self.__history_states = []
		self.__history_requests = []

	def __init_source(self, tacts):
		return Source(tacts=tacts)

	def __init_queue(self, max_requests):
		return Queue(max_requests=max_requests)

	def __get_channel(self, dhndl_prob):
		return Channel(dhndl_prob=dhndl_prob)

	@property
	def history_states(self):
		return self.__history_states
	
	@property
	def history_requests(self):
		return self.__history_requests

	def __add_history_state(self):
		self.__history_states.append(
			(
				self.__source.current_tact, 
				self.__queue.amount_of_requests, 
				1 if not self.__channel_1.is_free else 0, 
				1 if not self.__channel_2.is_free else 0
			)
		)
	
	def __add_history_request(self, request):
		self.__history_requests.append(request)

	def start(self, tacts):
		self.__history_states = []
		self.__history_requests = []

		for i in range(tacts):
			self.__add_history_state()
			self.__make_tact()

	def __make_tact(self):
		request = self.__channel_2.tact()
		if request:
			request.end()
		request = self.__channel_1.tact()
		if request:
			res = self.__channel_2.put_request(request)
			if not res:
				request.reject()
		self.__queue.tact()
		if self.__channel_1.is_free:
			request = self.__queue.pop_from_queue()
			if request:
				res = self.__channel_1.put_request(request)

		request = self.__source.tact()
		if request:
			self.__add_history_request(request)
			res = self.__channel_1.put_request(request)
			if not res:
				res = self.__queue.put_request(request)
				if not res:
					request.reject()














