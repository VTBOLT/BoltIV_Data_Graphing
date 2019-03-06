from digi.xbee.devices import XBeeDevice
import matplotlib.pyplot as plt
PORT = "COM6"
BAUD_RATE = 57600


def main():
	print(" +-----------------------------------------+")
	print(" | XBee Python Library Receive Data Sample |")
	print(" +-----------------------------------------+\n")

	device = XBeeDevice(PORT, BAUD_RATE)
	head = ["Time","SOC","FPV","H_Temp","L_Temp","H_Volt","L_Volt","P_Volt","Aux_Volt","IMU_X","IMU_y","IMU_z","GYRO_X","GYRO_Y","GYRO_Z"]
	try:
		device.open()

		def data_receive_callback(xbee_message):
			message = xbee_message.data.decode()
			message = message[1:-2]
			row = [s.strip() for s in message.split(',')]
			for i in range(len(row)):
				print("{0}: {1}".format(head[i],row[i]))
		device.add_data_received_callback(data_receive_callback)
		input()
	finally:
		if device is not None and device.is_open():
			device.close()

if __name__ == '__main__':
    main()