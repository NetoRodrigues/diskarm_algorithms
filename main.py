from Disk import Disk
from DiskArm import DiskArm

disk = Disk()
disk_arm = DiskArm()


def run():
    print("Disk created!")
    print("Initial request positions: {} ".format(disk.REQUESTS))

    while True:
        #disk_arm.move_SSTF( disk.REQUESTS )
        #disk_arm.move_CSCAN( disk.REQUESTS )
        disk_arm.move_SCAN( disk.REQUESTS )

        if disk_arm.position in disk.REQUESTS:
            disk.fulfill_request(disk_arm.position)
            print("Request {} fulfilled!".format(disk_arm.position))

        if disk.has_no_requests():
            break


if __name__ == '__main__':
    run()
