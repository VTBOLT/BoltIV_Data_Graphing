from digi.xbee.devices import XBeeDevice
from digi.xbee.exception import TimeoutException, InvalidPacketException
import matplotlib.pyplot as plt
import matplotlib.ticker as plticker
import matplotlib.animation as animation
from matplotlib import style
import numpy as np
PORT = "COM6"
BAUD_RATE = 57600
count = 0

def main():
	print(" +-----------------------------------------+")
	print(" |    Python Xbee Receive And Graph Data   |")
	print(" +-----------------------------------------+\n")

	device = XBeeDevice(PORT, BAUD_RATE)
	head = ["Time","State Of Charge","Full Pack Voltage","High Temp","Low Temp","High Voltage","Low Voltage", "RPM", "Aux Battery Voltage","X Acc","Y Acc","Z Acc","X Gyro","Y Gyro","Z Gyro","Z Gyro"]
	#head = ["Time","State Of Charge","Full Pack Voltage","High Temp","Low Temp","High Voltage","Low Voltage","Pump Voltage","Aux Battery Voltage","X Acc","Y Acc","Z Acc","X Gyro","Y Gyro","Z Gyro","Roll","Pitch","Yaw","Compass"]
	points = []
	edgePoints = []
	for row in head:
		edgePoints.append([float('inf'),float('-inf')])
		points.append([0])
	points[0][0]=1
	props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
	fig=plt.figure()
	ax1=fig.add_subplot(3,2,3)#SOC
	ax2=fig.add_subplot(3,3,2)#FPV
	ax3=fig.add_subplot(3,3,3)#TEMP
	ax4=fig.add_subplot(3,3,1)#Volt
	ax5=fig.add_subplot(3,3,8)#Aux/Pump
	ax6=fig.add_subplot(3,3,7)#Acc
	ax7=fig.add_subplot(3,3,9)#Gyro
	ax8=fig.add_subplot(3,2,4)#RPM
	checksum_err = 0
	def animate(i):
		line_count=points[0][-1]
		try:
			if len(points[0]) == len(points[1]):
				ax1.clear()
				ax1.plot(points[0],points[1],'k')
				textstr = '\n'.join((("Max: {}".format(edgePoints[1][1])),("Min: {}".format(edgePoints[1][0])), "Latest: {}".format(points[1][-1])))
				ax1.set_title(head[1])#State Of Charge
				ax1.text(0.02, 0.95, textstr, transform=ax1.transAxes, fontsize=14, verticalalignment='top', bbox=props)
				ax1.set_ylim([0,100])
				ax1.grid()
				ax1.xaxis.set_visible(False)
				ax1.hlines(95, line_count-200, line_count, colors='g', linestyles='dashed', label='')
				ax1.hlines(30, line_count-200, line_count, colors='y', linestyles='dashed', label='')
				ax1.hlines(15, line_count-200, line_count, colors='r', linestyles='dashed', label='')
			else:
				print("point0:{0}\tpoint1:{1}".format(len(points[0]), len(points[1])))
		except Exception as e:
			print(e)
			print('first one')
			pass
		try:	
			if len(points[0]) == len(points[2]):
				ax2.clear()
				ax2.plot(points[0],points[2],'g')
				textstr = '\n'.join((("Max: {}".format(edgePoints[2][1])),("Min: {}".format(edgePoints[2][0])), "Latest: {}".format(points[2][-1])))
				ax2.set_title(head[2])#Full Pack Voltage
				ax2.text(0.03, 0.95, textstr, transform=ax2.transAxes, fontsize=14, verticalalignment='top', bbox=props)
				ax2.set_ylim((200,750))
				ax2.grid()
				ax2.xaxis.set_visible(False)
				ax2.hlines(698, line_count-200, line_count, colors='b', linestyles='dashed', label='')
				ax2.hlines(597, line_count-200, line_count, colors='k', linestyles='dashed', label='')
				ax2.hlines(480, line_count-200, line_count, colors='r', linestyles='dashed', label='')
		except Exception as e:
			print(e)
			print('second one')
			pass
		try:	
			if (len(points[0]) == len(points[3])) and (len(points[0]) == len(points[4])):
				ax3.clear()
				ax3.plot(points[0],points[3],'r')
				ax3.plot(points[0],points[4],'b')
				textstr = '\n'.join((("Max: {}".format(edgePoints[3][1])),("Min: {}".format(edgePoints[4][0])), "Latest: {}".format(points[3][-1])))
				ax3.set_title("Min/Max Cell Temps")
				ax3.text(0.03, 0.95, textstr, transform=ax3.transAxes, fontsize=14, verticalalignment='top', bbox=props)
				ax3.xaxis.set_visible(False)
				ax3.set_ylim(20,90)
				ax3.grid()
				ax3.hlines(40, line_count-200, line_count, colors='g', linestyles='dashed', label='')
				ax3.hlines(60, line_count-200, line_count, colors='y', linestyles='dashed', label='')
				ax3.hlines(80, line_count-200, line_count, colors='r', linestyles='dashed', label='')
		except Exception as e:
			print(e)
			print('third one')
			pass
		try:	
			if (len(points[0]) == len(points[5])) and (len(points[0]) == len(points[6])):
				ax4.clear()
				ax4.plot(points[0],points[5],'r')
				ax4.plot(points[0],points[6],'b')
				textstr = '\n'.join((("Max: {}".format(edgePoints[5][1])),("Min: {}".format(edgePoints[6][0])), "Latest: {}".format(points[5][-1])))
				ax4.set_title("Min/Max Cell Volts")
				ax4.text(0.03, 0.95, textstr, transform=ax4.transAxes, fontsize=14, verticalalignment='top', bbox=props)
				ax4.xaxis.set_visible(False)
				ax4.grid()
				ax4.set_ylim(1,5)
				ax4.hlines(4.2, line_count-200, line_count, colors='g', linestyles='dashed', label='')
				ax4.hlines(3.8, line_count-200, line_count, colors='y', linestyles='dashed', label='')
				ax4.hlines(3.0, line_count-200, line_count, colors='r', linestyles='dashed', label='')
		except Exception as e:
			print(e)
			print('fourth one')
			pass
		try:	
			if (len(points[0]) == len(points[12])) and (len(points[0]) == len(points[13])) and (len(points[0]) == len(points[14])):
				ax5.cla()
				ax5.plot(points[12][-1],points[13][-1],'go')
				ax5.plot(points[12][-1],points[14][-1],'bo')
				textstr = '\n'.join((("Latest X: {}".format(points[12][-1])),("Latest Y: {}".format(points[13][-1])),("Latest Z: {}".format(points[14][-1]))))
				ax5.text(0.03, 0.95, textstr, transform=ax5.transAxes, fontsize=14, verticalalignment='top', bbox=props)
				ax5.set_title("IMU Gyro")
				ax5.set_xlim(-2,2)
				ax5.set_ylim(-2,2)
				ax5.hlines(-1, -1, 1, colors='g', linestyles='dashed', label='')
				ax5.hlines(1, -1, 1, colors='g', linestyles='dashed', label='')
				ax5.vlines(-1, -1, 1, colors='g', linestyles='dashed', label='')
				ax5.vlines(1, -1, 1, colors='g', linestyles='dashed', label='')
		except Exception as e:
			print(e)
			print('fifth one')
			pass
		try:	
			if (len(points[0]) == len(points[9])) and (len(points[0]) == len(points[10])) and (len(points[0]) == len(points[11])):
				ax6.cla()
				ax6.plot(points[9][-1],points[10][-1],'go')
				ax6.plot(points[9][-1],points[11][-1],'bo')
				textstr = '\n'.join((("Latest X: {}".format(points[9][-1])),("Latest Y: {}".format(points[10][-1])),("Latest Z: {}".format(points[11][-1]))))
				ax6.text(0.03, 0.95, textstr, transform=ax6.transAxes, fontsize=14, verticalalignment='top', bbox=props)
				ax6.set_title("IMU Lattitude")
				ax6.set_xlim(-2,2)
				ax6.set_ylim(-2,2)
				ax6.hlines(-1, -1, 1, colors='g', linestyles='dashed', label='')
				ax6.hlines(1, -1, 1, colors='g', linestyles='dashed', label='')
				ax6.vlines(-1, -1, 1, colors='g', linestyles='dashed', label='')
				ax6.vlines(1, -1, 1, colors='g', linestyles='dashed', label='')
		except Exception as e:
			print(e)
			print('sixth one')
			pass
		try:	
			if (len(points[0]) == len(points[8])) and (len(points[0]) == len(points[9])):
				ax7.cla()
				ax7.plot(points[0],points[8],'c')
				textstr = '\n'.join((("Max: {}".format(edgePoints[8][1])),("Min: {}".format(edgePoints[8][0])), "Latest: {}".format(points[8][-1])))
				ax7.text(0.03, 0.95, textstr, transform=ax7.transAxes, fontsize=14, verticalalignment='top', bbox=props)
				ax7.set_title("Aux Volt")
				ax7.set_ylim(0,20)
				ax7.grid()
				ax7.xaxis.set_visible(False)
		except Exception as e:
			print(e)
			print('seventh one')
			pass
		try:	
			if (len(points[0]) == len(points[7])):
				ax8.cla()
				ax8.plot(points[0],points[7],'c')
				wheelCir = 1.979 #in meters
				gearing= 55/14 #number of back sprocket teeth / front sprocket teeth
				velocity = float(points[7][-1])/60 *wheelCir / gearing #rpm/60*wheel circum/gearing   -> meters per second
				speed = round(velocity*2.23694,2) #convert meters per second to miles per hour
				textstr = '\n'.join((("Max: {}".format(edgePoints[7][1])),("Latest: {}".format(points[7][-1])), ("Speed(MPH): {}".format(speed))))
				ax8.text(0.02, 0.95, textstr, transform=ax8.transAxes, fontsize=14, verticalalignment='top', bbox=props)
				ax8.set_title("Motor RPM")
				ax8.xaxis.set_visible(False)
				ax8.set_ylim(0,12000)
				ax8.grid()
				ax8.hlines(10000, line_count-200, line_count, colors='g', linestyles='dashed', label='')
		except Exception as e:
			print(e)
			print('eigth one')
			pass
	try:
		device.open()
		def data_receive_callback(xbee_message):
			try:
				global count
				message = xbee_message.data.decode()
				row = [s.strip() for s in message.replace('\x00','').replace('\t','').split(',')]
				#print (row)
				if len(row) == (len(head)-1):
					points.append([])
					count +=1
					points[0].append(count)
					for i in range(len(row)):
						datapoint = (float(row[i]))
						if i == 0:
							datapoint = datapoint * 0.5
						elif i == 1:
							datapoint = datapoint * 0.1
						elif i == 4 or i == 5:
							datapoint = datapoint * 0.0001
						datapoint = round(datapoint, 1)
						points[i+1].append(datapoint)
						points[i] = points[i][-200:]
						if datapoint < edgePoints[i+1][0]:
							edgePoints[i+1][0] = datapoint
						if datapoint > edgePoints[i+1][1]:
							edgePoints[i+1][1] = datapoint
				else:
					print(row)
					print(len(row))
					print(len(head))
			except Exception as e:
				print(e)
				print('mesage receive')
				pass
		try:
			device.add_data_received_callback(data_receive_callback)
		except InvalidPacketException as e:
			self._log.error("Error processing packet '%s': %s" % (utils.hex_to_string(raw_packet), str(e)))
			pass
		ani = animation.FuncAnimation(fig, animate, interval=10)
		mng = plt.get_current_fig_manager()
		mng.window.state('zoomed')
		plt.show()
	finally:
		if device is not None and device.is_open():
			device.close()

if __name__ == '__main__':
    main()