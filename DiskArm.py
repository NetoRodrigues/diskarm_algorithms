import random
from settings import MIN_POSITION, MAX_POSITION


class DiskArm:

	def __init__(self):
		self.position = random.randrange(MIN_POSITION, MAX_POSITION, 1)
		print("Disk Arm created at {}".format(self.position))
		

	def move_SSTF(self, requests):
		closest = min(requests, key=lambda x:abs(x-self.position))
		if self.position > closest:
			self.position-= 1
		elif self.position < closest:
			self.position+= 1
		print("Disk Arm moved to position {}".format(self.position))

	def move_LOOK(self, requests):
		index = next((data[0] for data in enumerate(requests) if data[1] > self.position), None)
		if index is None:
			requests = list(reversed(requests))
			index = next(data[0] for data in enumerate(requests) if data[1] < self.position)
			
		if self.position > requests[index]:
			self.position-= 1
		elif self.position < requests[index]:
			self.position+= 1
		print("Disk Arm moved to position {}".format(self.position))

	def move_CLOOK(self, requests):
		index = next((data[0] for data in enumerate(requests) if data[1] > self.position), None)
		if index is None:
			self.position = min(requests)
		else:
			self.position+= 1
			
		print("Disk Arm moved to position {}".format(self.position))

	def move_CSCAN(self, requests):
		self.position+= 1
		if self.position > MAX_POSITION:
			self.position = MIN_POSITION

		print("Disk Arm moved to position {}".format(self.position))