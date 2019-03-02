from digi.xbee.devices import XBeeDevice
PORT = "COM6"
BAUD_RATE = 57600


def main():
	print(" +-----------------------------------------+")
	print(" | XBee Python Library Receive Data Sample |")
	print(" +-----------------------------------------+\n")

	device = XBeeDevice(PORT, BAUD_RATE)

	try:
		device.open()

		def data_receive_callback(xbee_message):
			head = ["Time","SOC","FPV","H_Temp","L_Temp","H_Volt","L_Volt","P_Volt","Aux_Volt","IMU"]
			message = xbee_message.data.decode()
			message = message[1:-2]
			row = [s.strip() for s in message.split(',')]
			for i in range(len(head)):
				print("{0}: {1}".format(head[i],row[i]))
		device.add_data_received_callback(data_receive_callback)

		print("Waiting for data...\n")
		input()

	finally:
		if device is not None and device.is_open():
			device.close()

if __name__ == '__main__':
    main()