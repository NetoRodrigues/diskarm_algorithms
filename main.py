from Disk import Disk
from DiskArm import DiskArm

disk = Disk()
disk_arm = DiskArm()


def run():
    tick = 0
    print("Disk created!")
    print("Initial request positions: {} ".format(disk.REQUESTS))

    while True:
        disk_arm.move()
        if disk_arm.position in disk.REQUESTS:
            disk.fulfill_request(disk_arm.position)
            print("Request {} fulfilled!".format(disk_arm.position))

        if disk.has_no_requests():
            break

        # Just in case we want dynamic request creation, not necessary
        # tick += 1
        # if tick % 25 == 0:
        #     disk.create_request()


if __name__ == '__main__':
    run()
