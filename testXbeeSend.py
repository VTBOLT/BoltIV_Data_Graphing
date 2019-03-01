from digi.xbee.devices import XBeeDevice
PORT = "COM5"
BAUD_RATE = 27600


def main():
    print(" +-----------------------------------------+")
    print(" | XBee Python Library Send Data Sample |")
    print(" +-----------------------------------------+\n")

    device = XBeeDevice(PORT, BAUD_RATE)

    try:
        device.open()
        device.send_data_broadcast("Hello XBee World!")

    finally:
        if device is not None and device.is_open():
            device.close()


if __name__ == '__main__':
    main()