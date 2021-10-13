from request import Request


class Source():
	def __init__(self, tacts=2):
		self.__tacts = tacts
		self.__current_tact = self.__tacts

	@property
	def current_tact(self):
		return self.__current_tact
	
	def tact(self):
		self.__current_tact -= 1
		if self.__current_tact == 0:
			self.__current_tact = self.__tacts
			return Request()
		else:
			return None