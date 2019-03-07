from digi.xbee.devices import XBeeDevice
import matplotlib.pyplot as plt
import matplotlib.ticker as plticker
import numpy as np
PORT = "COM5"
BAUD_RATE = 57600
def main():
	print(" +-----------------------------------------+")
	print(" | XBee Python Library Receive Data Sample |")
	print(" +-----------------------------------------+\n")

	device = XBeeDevice(PORT, BAUD_RATE)
	head = ["Time","SOC","FPV","H_Temp","L_Temp","H_Volt","L_Volt","P_Volt","Aux_Volt","IMU","anotherone"]
	points = []
	edgePoints = []
	for row in head:
		edgePoints.append([float('inf'),float('-inf')])
		points.append([0])

	props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
	ax1=plt.subplot(313)
	ax1.set_title(head[9])
	ax2=plt.subplot(321)
	ax2.set_title(head[2])
	ax3=plt.subplot(322)
	ax3.set_title("Min/Max Cell Temps")
	ax4=plt.subplot(323)
	ax4.set_title("Min/Max Cell Volts")
	ax5=plt.subplot(324)
	ax5.set_title("Aux Volt and Pump Volt")
	plt.ion()
	plt.show()
	checksum_err = 0;
	try:
		device.open()

		def data_receive_callback(xbee_message):
			try:
				message = xbee_message.data.decode()
				message = message[1:-2]
				row = [s.strip() for s in message.split(',')]
				points.append([])
				for i in range(len(row)):
					points[i].append(row[i])
					if float(row[i]) < edgePoints[i][0]:
						edgePoints[i][0] = float(row[i])
					if float(row[i]) > edgePoints[i][1]:
						edgePoints[i][1] = float(row[i])
			except Exception as e:
				print(e)
				pass
		device.add_data_received_callback(data_receive_callback)

		print("Waiting for data...\n")
		while True:
			line_count = float(points[0][-1])
			try:
				if len(points[0]) == len(points[9]):
					ax1.cla()
					if line_count<100:
						ax1.plot(points[0],points[9],'k')
					else:
						ax1.plot(points[0][-100:-1],points[9][-100:-1],'k')
					textstr = '\n'.join((("Max: {}".format(edgePoints[9][1])),("Min: {}".format(edgePoints[9][0])), "Latest: {}".format(points[9][-1])))
					ax1.text(0.05, 0.95, textstr, transform=ax1.transAxes, fontsize=14, verticalalignment='top', bbox=props)
					ax1.xaxis.set_major_locator(plticker.MultipleLocator(base = 20.0))
					ax1.yaxis.set_major_locator(plticker.MultipleLocator(base = 20.0))
			except Exception as e:
				print(e)
				pass
			try:	
				if len(points[0]) == len(points[2]):
					ax2.cla()
					if line_count<100:
						ax2.plot(points[0],points[2],'g')
					else:
						ax2.plot(points[0][-100:-1],points[2][-100:-1],'g')
					textstr = '\n'.join((("Max: {}".format(edgePoints[2][1])),("Min: {}".format(edgePoints[2][0])), "Latest: {}".format(points[2][-1])))
					ax2.text(0.05, 0.95, textstr, transform=ax2.transAxes, fontsize=14, verticalalignment='top', bbox=props)
					ax2.xaxis.set_major_locator(plticker.MultipleLocator(base = 20.0))
					ax2.yaxis.set_major_locator(plticker.MultipleLocator(base = 20.0))
			except Exception as e:
				print(e)
				pass	
			try:	
				if (len(points[0]) == len(points[3])) and (len(points[0]) == len(points[4])):
					ax3.cla()
					if line_count<100:
						ax3.plot(points[0],points[3],'r')
						ax3.plot(points[0],points[4],'b')
					else:
						ax3.plot(points[0][-100:-1],points[3][-100:-1],'r')
						ax3.plot(points[0][-100:-1],points[4][-100:-1],'b')
					textstr = '\n'.join((("Max: {}".format(edgePoints[3][1])),("Min: {}".format(edgePoints[3][0])), "Latest: {}".format(points[3][-1])))
					ax3.text(0.05, 0.95, textstr, transform=ax3.transAxes, fontsize=14, verticalalignment='top', bbox=props)
					ax3.xaxis.set_major_locator(plticker.MultipleLocator(base = 20.0))
					ax3.yaxis.set_major_locator(plticker.MultipleLocator(base = 20.0))
			except Exception as e:
				print(e)
				pass	
			try:	
				if (len(points[0]) == len(points[5])) and (len(points[0]) == len(points[6])):
					ax4.cla()
					if line_count<100:
						ax4.plot(points[0],points[5],'r')
						ax4.plot(points[0],points[6],'b')
					else:
						ax4.plot(points[0][-100:-1],points[5][-100:-1],'r')
						ax4.plot(points[0][-100:-1],points[6][-100:-1],'b')
					textstr = '\n'.join((("Max: {}".format(edgePoints[5][1])),("Min: {}".format(edgePoints[5][0])), "Latest: {}".format(points[5][-1])))
					ax4.text(0.05, 0.95, textstr, transform=ax4.transAxes, fontsize=14, verticalalignment='top', bbox=props)
					ax4.xaxis.set_major_locator(plticker.MultipleLocator(base = 20.0))
					ax4.yaxis.set_major_locator(plticker.MultipleLocator(base = 20.0))
			except Exception as e:
				print(e)
				pass
			try:	
				if (len(points[0]) == len(points[7])) and (len(points[0]) == len(points[8])):
					ax5.cla()
					if line_count<100:
						ax5.plot(points[0],points[7],'c')
						ax5.plot(points[0],points[8],'m')
					else:
						ax5.plot(points[0][-100:-1],points[7][-100:-1],'c')
						ax5.plot(points[0][-100:-1],points[8][-100:-1],'m')
					textstr = '\n'.join((("Max: {}".format(edgePoints[7][1])),("Min: {}".format(edgePoints[7][0])), "Latest: {}".format(points[7][-1])))
					ax5.text(0.05, 0.95, textstr, transform=ax5.transAxes, fontsize=14, verticalalignment='top', bbox=props)
					ax5.xaxis.set_major_locator(plticker.MultipleLocator(base = 20.0))
					ax5.yaxis.set_major_locator(plticker.MultipleLocator(base = 20.0))
			except Exception as e:
				print(e)
				pass
			plt.draw()
			plt.pause(0.0001)
	finally:
		if device is not None and device.is_open():
			device.close()

if __name__ == '__main__':
    main()