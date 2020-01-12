'''
Define :
Interface : TouchScreenLaptop : with 2 methods scroll and click

Class : HP : an abstract class inheriting TouchScreenLaptop and implementing scroll method
Class : HPNotebook : class implementing click, can override scroll

Similarly,

Class : Dell : an abstract class inheriting TouchScreenLaptop and implementing scroll
Class :	DellNotebook : class implement click, can override scroll

'''


from abc import abstractmethod 					#decorator
from abc import ABC 							      #class


class TouchScreenLaptop(ABC):
	def __init__(self):
		print("TouchScreenLaptop Constructor called ")

	@abstractmethod
	def scroll(self):
		pass

	@abstractmethod
	def click(self):
		pass


class HP(TouchScreenLaptop):
	def __init__(self):
		print("HP Constructor called ")
		super().__init__()

	def scroll():
		print("HP Class : Implementing scroll method")


class DELL(TouchScreenLaptop):
	def __init__(self):
		print("DELL Constructor called ")
		super().__init__()

	def scroll(self):
		print("DELl CLass : Implementing scroll method")


class HPNotebook(HP):
	def __init__(self):
		print("HPNotebook Constructor called ")
		super().__init()

	def scroll(self):
		print("HPNotebook Class: Overriding scroll method ")

	def click(self):
		print("HPNotebook Class: Implementing click method")


class DELLNotebook(DELL):
	def __init__(self):
		print("DELLNotebook Constructor called ")
		super().__init__()

	def scroll(self):
		print("DELLNotebook Class: Overriding scroll method")

	def click(self):
		print("DELLNotebook Class : Implementing click method")




if __name__ == "__main__":
	dn1 = DELLNotebook()



'''
#output
>python main.py
DELLNotebook Constructor called
DELL Constructor called
TouchScreenLaptop Constructor called
'''

'''
#If we try to create object of class HP :
hp1 = HP()
#output
TypeError: Can't instantiate abstract class HP with abstract methods click
#reason
As we have not implemented click method
'''
