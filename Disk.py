# Disk range: 0-39
# Initial request positions: 1, 9, 12, 16, 34, 36
import random

MIN_POSITION = 0
MAX_POSITION = 39


class Disk:

    def __init__(self):
        random.seed(1)
        self.REQUESTS = [1, 9, 12, 16, 34, 36]

    def create_request(self):
        request_position = random.randrange(MIN_POSITION,MAX_POSITION,1)
        if request_position not in self.REQUESTS:
            self.REQUESTS.append(request_position)

    def fulfill_request(self, request_position):
        self.REQUESTS.remove(request_position)
