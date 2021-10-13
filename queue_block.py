class Queue():
	def __init__(self, max_requests=0):
		self.__max_requests = max_requests
		self.__requests_in_queue = []

	@property
	def amount_of_requests(self):
		return len(self.__requests_in_queue)
	
	def put_request(self, request):
		if len(self.__requests_in_queue) < self.__max_requests:
			request.put_in_queue()
			self.__requests_in_queue.insert(0, request)
			return True
		else:
			return False

	def tact(self):
		for request in self.__requests_in_queue:
			request.inc_tacts()
			request.inc_tacts_in_queue()

	def pop_from_queue(self):
		if self.__requests_in_queue:
			request = self.__requests_in_queue.pop()
			request.get_out_of_queue()
			return request

