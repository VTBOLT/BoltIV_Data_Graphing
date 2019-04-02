from digi.xbee.devices import XBeeDevice
import matplotlib.pyplot as plt
import matplotlib.ticker as plticker
import numpy as np
PORT = "COM7"
BAUD_RATE = 57600
count = 0
def main():
	print(" +-----------------------------------------+")
	print(" | XBee Python Library Receive Data Sample |")
	print(" +-----------------------------------------+\n")

	device = XBeeDevice(PORT, BAUD_RATE)
	head = ["Time","State Of Charge","Full Pack Voltage","High Temp","Low Temp","High Voltage","Low Voltage","X Latitude","Y Latitutde","Z Latitude","X Gyro","Y Gyro","Z Gyro","Pump Voltage","Aux Battery Voltage"]
	points = []
	edgePoints = []
	for row in head:
		edgePoints.append([float('inf'),float('-inf')])
		points.append([0])
	points[0][0]=1
	props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
	ax1=plt.subplot(331)
	ax2=plt.subplot(332)
	ax3=plt.subplot(333)
	ax4=plt.subplot(334)
	ax5=plt.subplot(335)
	ax6=plt.subplot(336)
	ax7=plt.subplot(325)
	ax8=plt.subplot(326)
	plt.ion()
	plt.show()
	checksum_err = 0
	
	try:
		device.open()

		def data_receive_callback(xbee_message):
			try:
				global count
				message = xbee_message.data.decode()
				row = [s.strip() for s in message.replace('\x00','').split(',')]
				points.append([])
				
				count +=1
				points[0].append(count)
				
				for i in range(len(row)):
					points[i+1].append(row[i])
					if float(row[i]) < edgePoints[i+1][0]:
						edgePoints[i+1][0] = float(row[i])
					if float(row[i]) > edgePoints[i+1][1]:
						edgePoints[i+1][1] = float(row[i])
			except Exception as e:
				print(e)
				print('mesage receive')
				pass
		device.add_data_received_callback(data_receive_callback)

		print("Waiting for data...\n")
		while True:
			line_count = float(points[0][-1])
			try:
				if len(points[0]) == len(points[1]):
					ax1.cla()
					if count<100:
						ax1.plot(points[0],points[1],'k')
					else:
						ax1.plot(points[0][-100:-1],points[1][-100:-1],'k')
					textstr = '\n'.join((("Max: {}".format(edgePoints[1][1])),("Min: {}".format(edgePoints[1][0])), "Latest: {}".format(points[1][-1])))
					ax1.set_title(head[1])#State Of Charge
					ax1.text(0.05, 0.95, textstr, transform=ax1.transAxes, fontsize=14, verticalalignment='top', bbox=props)
					#ax1.xaxis.set_major_locator(plticker.MultipleLocator(base = 20.0))
					#ax1.yaxis.set_major_locator(plticker.MultipleLocator(base = 20.0))
			except Exception as e:
				print(e)
				print('first one')
				pass
			try:	
				if len(points[0]) == len(points[2]):
					ax2.cla()
					if count<100:
						ax2.plot(points[0],points[2],'g')
					else:
						ax2.plot(points[0][-100:-1],points[2][-100:-1],'g')
					textstr = '\n'.join((("Max: {}".format(edgePoints[2][1])),("Min: {}".format(edgePoints[2][0])), "Latest: {}".format(points[2][-1])))
					ax2.set_title(head[2])#Full Pack Voltage
					ax2.text(0.05, 0.95, textstr, transform=ax2.transAxes, fontsize=14, verticalalignment='top', bbox=props)
					#ax2.xaxis.set_major_locator(plticker.MultipleLocator(base = 20.0))
					#ax2.yaxis.set_major_locator(plticker.MultipleLocator(base = 20.0))
			except Exception as e:
				print(e)
				print('second one')
				pass	
			try:	
				if (len(points[0]) == len(points[3])) and (len(points[0]) == len(points[4])):
					ax3.cla()
					if count<100:
						ax3.plot(points[0],points[3],'r')
						ax3.plot(points[0],points[4],'b')
					else:
						ax3.plot(points[0][-100:-1],points[3][-100:-1],'r')
						ax3.plot(points[0][-100:-1],points[4][-100:-1],'b')
					textstr = '\n'.join((("Max: {}".format(edgePoints[3][1])),("Min: {}".format(edgePoints[4][0])), "Latest: {}".format(points[3][-1])))
					ax3.set_title("Min/Max Cell Temps")
					ax3.text(0.05, 0.95, textstr, transform=ax3.transAxes, fontsize=14, verticalalignment='top', bbox=props)
					#ax3.xaxis.set_major_locator(plticker.MultipleLocator(base = 20.0))
					#ax3.yaxis.set_major_locator(plticker.MultipleLocator(base = 20.0))
			except Exception as e:
				print(e)
				print('third one')
				pass	
			try:	
				if (len(points[0]) == len(points[5])) and (len(points[0]) == len(points[6])):
					ax4.cla()
					if count<100:
						ax4.plot(points[0],points[5],'r')
						ax4.plot(points[0],points[6],'b')
					else:
						ax4.plot(points[0][-100:-1],points[5][-100:-1],'r')
						ax4.plot(points[0][-100:-1],points[6][-100:-1],'b')
					textstr = '\n'.join((("Max: {}".format(edgePoints[5][1])),("Min: {}".format(edgePoints[6][0])), "Latest: {}".format(points[5][-1])))
					ax4.set_title("Min/Max Cell Volts")
					ax4.text(0.05, 0.95, textstr, transform=ax4.transAxes, fontsize=14, verticalalignment='top', bbox=props)
					#ax4.xaxis.set_major_locator(plticker.MultipleLocator(base = 20.0))
					#ax4.yaxis.set_major_locator(plticker.MultipleLocator(base = 20.0))
			except Exception as e:
				print(e)
				print('fourth one')
				pass
			try:	
				if (len(points[0]) == len(points[7])) and (len(points[0]) == len(points[8])) and (len(points[0]) == len(points[9])):
					ax5.cla()
					if count<100:
						ax5.plot(points[0],points[7],'c')
						ax5.plot(points[0],points[8],'m')
						ax5.plot(points[0],points[9],'b')
					else:
						ax5.plot(points[0][-100:-1],points[7][-100:-1],'c')
						ax5.plot(points[0][-100:-1],points[8][-100:-1],'m')
						ax5.plot(points[0][-100:-1],points[9][-100:-1],'b')
					textstr = '\n'.join((("Latest X: {}".format(points[7][-1])),("Latest Y: {}".format(points[8][-1])),("Latest Z: {}".format(points[9][-1]))))
					ax5.text(0.05, 0.95, textstr, transform=ax5.transAxes, fontsize=14, verticalalignment='top', bbox=props)
					ax5.set_title("IMU Lattitude")
					#ax5.xaxis.set_major_locator(plticker.MultipleLocator(base = 20.0))
					#ax5.yaxis.set_major_locator(plticker.MultipleLocator(base = 20.0))
			except Exception as e:
				print(e)
				print('fifth one')
				pass
			try:	
				if (len(points[0]) == len(points[10])) and (len(points[0]) == len(points[11])) and (len(points[0]) == len(points[12])):
					ax6.cla()
					if count<100:
						ax6.plot(points[0],points[10],'c')
						ax6.plot(points[0],points[11],'m')
						ax6.plot(points[0],points[12],'b')
					else:
						ax6.plot(points[0][-100:-1],points[10][-100:-1],'c')
						ax6.plot(points[0][-100:-1],points[11][-100:-1],'m')
						ax6.plot(points[0][-100:-1],points[12][-100:-1],'b')
					textstr = '\n'.join((("Latest X: {}".format(points[10][-1])),("Latest Y: {}".format(points[11][-1])),("Latest Z: {}".format(points[12][-1]))))
					ax6.text(0.05, 0.95, textstr, transform=ax6.transAxes, fontsize=14, verticalalignment='top', bbox=props)
					ax6.set_title("IMU Gyro")
					#ax6.xaxis.set_major_locator(plticker.MultipleLocator(base = 20.0))
					#ax6.yaxis.set_major_locator(plticker.MultipleLocator(base = 20.0))
			except Exception as e:
				print(e)
				print('sixth one')
				pass
			try:	
				if (len(points[0]) == len(points[13])) and (len(points[0]) == len(points[14])):
					ax7.cla()
					if count<100:
						ax7.plot(points[0],points[13],'c')
						ax7.plot(points[0],points[14],'m')
					else:
						ax7.plot(points[0][-100:-1],points[13][-100:-1],'c')
						ax7.plot(points[0][-100:-1],points[14][-100:-1],'m')
					textstr = '\n'.join((("Max: {}".format(edgePoints[13][1])),("Min: {}".format(edgePoints[13][0])), "Latest: {}".format(points[5][-1])))
					ax7.text(0.05, 0.95, textstr, transform=ax7.transAxes, fontsize=14, verticalalignment='top', bbox=props)
					ax7.set_title("Aux Volt and Pump Volt")
					#ax7.xaxis.set_major_locator(plticker.MultipleLocator(base = 20.0))
					#ax7.yaxis.set_major_locator(plticker.MultipleLocator(base = 20.0))
			except Exception as e:
				print(e)
				print('seventh one')
				pass
			try:	
				if (len(points[0]) == len(points[14])):
					ax8.cla()
					textstr = "null"
					ax8.text(0.05, 0.95, textstr, transform=ax8.transAxes, fontsize=14, verticalalignment='top', bbox=props)
					ax8.set_title("Motor RPM")
					#ax8.xaxis.set_major_locator(plticker.MultipleLocator(base = 20.0))
					#ax8.yaxis.set_major_locator(plticker.MultipleLocator(base = 20.0))
			except Exception as e:
				print(e)
				print('eigth one')
				pass
			plt.draw()
			plt.pause(0.0001)
	finally:
		if device is not None and device.is_open():
			device.close()

if __name__ == '__main__':
    main()