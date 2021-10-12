class Request:
	def __init__(self):
		self.__tacts = 0
		self.__is_rejected = False
		self.__tacts_in_queue = 0
		self.__is_in_queue = False
		self.__is_ended = False

	@property
	def tacts(self):
		return self.__tacts

	def inc_tacts(self):
		if (not self.__is_rejected) and (not self.__is_ended):
			self.__tacts += 1

	@property
	def is_rejected(self):
		return self.__is_rejected

	def reject(self):
		self.__is_rejected = True

	@property
	def tacts_in_queue(self):
		return self.__tacts_in_queue
	
	def inc_tacts_in_queue(self):
		if (self.__is_in_queue) and (not self.__is_rejected):
			self.__tacts_in_queue += 1

	@property
	def is_in_queue(self):
		return self.__is_in_queue

	def put_in_queue(self):
		if (not self.__is_in_queue) and (not self.__is_rejected):
			self.__is_in_queue = True

	def get_out_of_queue(self):
		if (self.__is_in_queue) and (not self.__is_rejected):
			self.__is_in_queue = False
	
	@property
	def is_ended(self):
		return self.__is_ended

	def end(self):
		if (not self.__is_rejected) and (not self.__is_in_queue):
			self.__is_ended = True

	