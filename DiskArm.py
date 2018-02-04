import random
from settings import MIN_POSITION, MAX_POSITION


class DiskArm:

    def __init__(self):
        self.position = random.randrange(MIN_POSITION, MAX_POSITION, 1)
        print("Disk Arm created at {}".format(self.position))
        self.mode = 'test'

    def move(self):
        if self.mode == 'test':
            self.position+= 1
        if self.position > MAX_POSITION:
            self.position = MIN_POSITION
        print("Disk Arm moved to position {}".format(self.position))