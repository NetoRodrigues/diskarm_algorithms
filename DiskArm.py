import random
import settings


class DiskArm:

	def __init__(self, policy):
		self.position = random.randrange(settings.MIN_POSITION, settings.MAX_POSITION, 1)
		self.policy = policy
		if self.policy == settings.SSTF:
			print 'DiskArm policy: SSTF'
		if self.policy == settings.LOOK:
			print 'DiskArm policy: LOOK'
		if self.policy == settings.CLOOK:
			print 'DiskArm policy: CLOOK'
		if self.policy == settings.CSCAN:
			print 'DiskArm policy: CSCAN'			
		print("Disk Arm created at {}".format(self.position))
		

	def move(self, requests):
		if self.policy == settings.SSTF:
			return self.move_SSTF(requests)
		if self.policy == settings.LOOK:
			return self.move_LOOK(requests)
		if self.policy == settings.CLOOK:
			return self.move_CLOOK(requests)
		if self.policy == settings.CSCAN:
			return self.move_CSCAN(requests)

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
		if self.position > settings.MAX_POSITION:
			self.position = settings.MIN_POSITION

		print("Disk Arm moved to position {}".format(self.position))