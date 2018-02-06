import random
from settings import MIN_POSITION, MAX_POSITION


class DiskArm:

	def __init__(self):
		self.position = random.randrange(MIN_POSITION, MAX_POSITION, 1)
		print("Disk Arm created at {}".format(self.position))
		#self.mode = 'test'

	'''
	def move(self):
		if self.mode == 'test':
			self.position+= 1
		if self.position > MAX_POSITION:
			self.position = MIN_POSITION
		print("Disk Arm moved to position {}".format(self.position))
	'''

	def move_SSTF(self, requests):
		closest = min(requests, key=lambda x:abs(x-self.position))
		self.position = closest
		print("Disk Arm moved to position {}".format(self.position))

	def move_SCAN(self, requests):
		index = next((data[0] for data in enumerate(requests) if data[1] > self.position), None)
		if index is None:
			requests = list(reversed(requests))
			index = next(data[0] for data in enumerate(requests) if data[1] < self.position)
			
		self.position = requests[index]
		print("Disk Arm moved to position {}".format(self.position))

	def move_CSCAN(self, requests):
		index = next((data[0] for data in enumerate(requests) if data[1] > self.position), 0)
		self.position = requests[index]
		print("Disk Arm moved to position {}".format(self.position))