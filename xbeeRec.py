from digi.xbee.devices import XBeeDevice
PORT = "COM6"
BAUD_RATE = 57600


def main():
	print(" +-----------------------------------------+")
	print(" | XBee Python Library Receive Data Sample |")
	print(" +-----------------------------------------+\n")

	device = XBeeDevice(PORT, BAUD_RATE)
	head = ["State Of Charge","Full Pack Voltage","High Temp","Low Temp","High Voltage","Low Voltage", "RPM", "Aux Battery Voltage","X Acc","Y Acc","Z Acc","X Gyro","Y Gyro","Z Gyro","Z Gyro","Roll","Pitch","Yaw"]
	
	try:
		device.open()

		def data_receive_callback(xbee_message):
			message = xbee_message.data.decode()
			print(message)
			# row = [s.strip() for s in message.split(',')]
			# for i in range(len(row)):
				# print("{0}: {1}".format(head[i],row[i]))
		device.add_data_received_callback(data_receive_callback)
		input()
	finally:
		if device is not None and device.is_open():
			device.close()

if __name__ == '__main__':
    main()