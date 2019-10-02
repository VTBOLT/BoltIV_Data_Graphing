from digi.xbee.devices import XBeeDevice
from digi.xbee.exception import TimeoutException, InvalidPacketException
import matplotlib.pyplot as plt
import matplotlib.ticker as plticker
import matplotlib.animation as animation
from matplotlib import style
import numpy as np
import sys, os

class XbeeDataGrapher():
	def __init__(self):
		self.count = 0
		self.points = [[]]
		self.edge_points = [[]]
		self.points[0].append([1])
		self.props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
		self.head = ["Time","State Of Charge","Full Pack Voltage","High Temp","Low Temp",
		"High Voltage","Low Voltage", "RPM","Motor Temp","Current","Torque","Driver Temp",
		"Aux Battery Voltage","X Acc","Y Acc","Z Acc","X Gyro","Y Gyro","Z Gyro","Roll","Pitch"]

	def xbee_setup(self, com = "COM8", baud = 57600):
		self.device = XBeeDevice(com, baud)
		self.device.open()
		self.device.add_data_received_callback(self._data_receive_callback)

	
	def xbee_close(self):
		self.device.close()

	def graph_setup(self):
		
		fig = plt.figure()
		
		self.soc_plot=fig.add_subplot(3,4,5)#SOC
		self.fpv_plot = fig.add_subplot(3,3,2)#FPV
		self.temp_plot = fig.add_subplot(3,3,3)#TEMP
		self.voltage_plot = fig.add_subplot(3,4,6)#Volt
		self.motor_mc_temp_plot = fig.add_subplot(3,3,8)#Motor/MC temp #Angle   , projection='polar'
		self.power_plot = fig.add_subplot(3,3,7)#Power #Acc
		self.aux_bat_voltage_plot = fig.add_subplot(3,3,9)#Aux
		self.rpm_plot = fig.add_subplot(3,2,4)#RPM
		self.torque_plot = fig.add_subplot(3,3,1)#Torque, Current

		animation.FuncAnimation(fig, self.animate, interval=10)


	
	def animate(self):
		line_count=self.points[0][-1]
		try:
			if len(self.points[0]) == len(self.points[1]):
				self._graph_soc(line_count)
			else:
				print("point0:{0}\tpoint1:{1}".format(len(self.points[0]), len(self.points[1])))
		except Exception as e:
			print(e)
			print('first plot')
			pass
		try:	
			if len(self.points[0]) == len(self.points[2]):
				self._graph_fpv(line_count)
		except Exception as e:
			print(e)
			print('second plot')
			pass
		try:	
			if (len(self.points[0]) == len(self.points[3])) and (len(self.points[0]) == len(self.points[4])):
				self._graph_temp(line_count)
		except Exception as e:
			print(e)
			print('third plot')
			pass
		try:	
			if (len(self.points[0]) == len(self.points[5])) and (len(self.points[0]) == len(self.points[6])):
				self._graph_voltage(line_count)
		except Exception as e:
			print(e)
			print('fourth plot')
			pass
		try:
			if (len(self.points[0]) == len(self.points[8])) and (len(self.points[0]) == len(self.points[11])):
				self._graph_motor_mc_temp(line_count)
		except Exception as e:
			print(e)
			print('fifth plot')
			pass
		try:	
			if (len(self.points[0]) == len(self.points[9])) and (len(self.points[0]) == len(self.points[2])):
				self._graph_power(line_count)
		except Exception as e:
			print(e)
			print('sixth plot')
			pass
		try:	
			if (len(self.points[0]) == len(self.points[12])):
				self._graph_aux_bat_voltage(line_count)
		except Exception as e:
			print(e)
			print('seventh plot')
			pass
		try:	
			if (len(self.points[0]) == len(self.points[7])):
				self._graph_rpm(line_count)
		except Exception as e:
			print(e)
			print('eigth plot')
			pass
		try:	
			if (len(self.points[0]) == len(self.points[9])) and (len(self.points[0]) == len(self.points[10])):
				self._graph_torque(line_count)
		except Exception as e:
			print(e)
			print('ninth plot')
			pass

	def _data_receive_callback(self, xbee_message):
		try:
			message = xbee_message.data.decode()
			row = [s.strip() for s in message.replace('\x00','').replace('\t','').split(',')]
			if len(row) == (len(self.head)-1):
				self.points.append([])
				self.count +=1
				self.points[0].append(self.count)
				for i in range(len(row)):
					datapoint = (float(row[i]))
					if i == 0:
						datapoint = datapoint * 0.5
					elif i == 1 or i==9 or i==10:
						datapoint = datapoint * 0.1
					elif i == 4 or i == 5:
						datapoint = datapoint * 0.0001
					datapoint = round(datapoint, 2)
					self.points[i].append(datapoint)
					self.points[i] = self.points[i][-200:]
					if len(self.edge_points[i]) == 0:
						self.edge_points.append([datapoint, datapoint])
					else:
						if datapoint < self.edge_points[i][0]:
							self.edge_points[i][0] = datapoint
						if datapoint > self.edge_points[i][1]:
							self.edge_points[i][1] = datapoint
			else:
				print(row)
				print(len(row))
				print(len(self.head))

		except Exception as e:		
			exc_type, exc_obj, exc_tb = sys.exc_info()
			fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
			print(exc_type, fname, exc_tb.tb_lineno)
			print(e)
			print('mesage receive')
			pass
	
	def _graph_soc(self, line_count):
		self.soc_plot.clear()
		self.soc_plot.plot(self.points[0],self.points[1],'k')
		textstr = '\n'.join((("Max: {}".format(self.edge_points[1][1])),("Min: {}".format(self.edge_points[1][0])), "Latest: {}".format(self.points[1][-1])))
		self.soc_plot.set_title(self.head[1])#State Of Charge
		self.soc_plot.text(0.02, 0.95, textstr, transform=self.soc_plot.transAxes, fontsize=14, verticalalignment='top', bbox=self.props)
		self.soc_plot.set_ylim([0,100])
		self.soc_plot.grid()
		self.soc_plot.xaxis.set_visible(False)
		self.soc_plot.hlines(95, line_count-200, line_count, colors='g', linestyles='dashed', label='')
		self.soc_plot.hlines(30, line_count-200, line_count, colors='y', linestyles='dashed', label='')
		self.soc_plot.hlines(15, line_count-200, line_count, colors='r', linestyles='dashed', label='')
	
	def _graph_fpv(self, line_count):
		self.fpv_plot.clear()
		self.fpv_plot.plot(self.points[0],self.points[2],'g')
		textstr = '\n'.join((("Max: {}".format(self.edge_points[2][1])),("Min: {}".format(self.edge_points[2][0])), "Latest: {}".format(self.points[2][-1])))
		self.fpv_plot.set_title(self.head[2])#Full Pack Voltage
		self.fpv_plot.text(0.03, 0.95, textstr, transform=self.fpv_plot.transAxes, fontsize=14, verticalalignment='top', bbox=self.props)
		self.fpv_plot.set_ylim((350,750))
		self.fpv_plot.grid()
		self.fpv_plot.xaxis.set_visible(False)
		self.fpv_plot.hlines(698, line_count-200, line_count, colors='b', linestyles='dashed', label='')
		self.fpv_plot.hlines(597, line_count-200, line_count, colors='k', linestyles='dashed', label='')
		self.fpv_plot.hlines(480, line_count-200, line_count, colors='r', linestyles='dashed', label='')

	def _graph_temp(self, line_count):
		self.temp_plot.clear()
		self.temp_plot.plot(self.points[0],self.points[3],'r')
		self.temp_plot.plot(self.points[0],self.points[4],'b')
		textstr = '\n'.join((("Max cell: {}".format(self.points[3][-1])),("Min cell: {}".format(self.points[4][-1]))))
		self.temp_plot.set_title("Cell Temps")
		self.temp_plot.text(0.03, 0.95, textstr, transform=self.temp_plot.transAxes, fontsize=14, verticalalignment='top', bbox=self.props)
		self.temp_plot.xaxis.set_visible(False)
		self.temp_plot.set_ylim(20,90)
		self.temp_plot.grid()
		self.temp_plot.hlines(40, line_count-200, line_count, colors='g', linestyles='dashed', label='')
		self.temp_plot.hlines(60, line_count-200, line_count, colors='y', linestyles='dashed', label='')
		self.temp_plot.hlines(80, line_count-200, line_count, colors='r', linestyles='dashed', label='')

	def _graph_voltage(self, line_count):
		self.voltage_plot.clear()
		self.voltage_plot.plot(self.points[0],self.points[5],'r')
		self.voltage_plot.plot(self.points[0],self.points[6],'b')
		textstr = '\n'.join((("Max: {}".format(self.points[5][-1])),("Min: {}".format(self.points[6][-1]))))
		self.voltage_plot.set_title("Min/Max Cell Volts")
		self.voltage_plot.text(0.03, 0.95, textstr, transform=self.voltage_plot.transAxes, fontsize=14, verticalalignment='top', bbox=self.props)
		self.voltage_plot.xaxis.set_visible(False)
		self.voltage_plot.grid()
		self.voltage_plot.set_ylim(1,5)
		self.voltage_plot.hlines(4.2, line_count-200, line_count, colors='g', linestyles='dashed', label='')
		self.voltage_plot.hlines(3.8, line_count-200, line_count, colors='y', linestyles='dashed', label='')
		self.voltage_plot.hlines(3.0, line_count-200, line_count, colors='r', linestyles='dashed', label='')

	def _graph_motor_mc_temp(self, line_count):
		self.motor_mc_temp_plot.cla()
		self.motor_mc_temp_plot.plot(self.points[0],self.points[8], 'k')
		self.motor_mc_temp_plot.plot(self.points[0],self.points[11], 'b')
		textstr = '\n'.join((("Motor Temp: {}".format(self.points[8][-1])),("MC Temp: {}".format(self.points[11][-1]))))
		self.motor_mc_temp_plot.text(0.03, 0.95, textstr, transform=self.motor_mc_temp_plot.transAxes, fontsize=14, verticalalignment='top', bbox=self.props)
		self.motor_mc_temp_plot.set_title("Motor/ Motor Controller Temp")
		self.motor_mc_temp_plot.grid()
		self.motor_mc_temp_plot.set_ylim(20,180)
		self.motor_mc_temp_plot.hlines(80, line_count-200, line_count, colors='y', linestyles='dashed', label='')
		self.motor_mc_temp_plot.hlines(100, line_count-200, line_count, colors='r', linestyles='dashed', label='')
		self.motor_mc_temp_plot.hlines(170, line_count-200, line_count, colors='r', linestyles='dashed', label='')
		self.motor_mc_temp_plot.xaxis.set_visible(False)
	
	def _graph_power(self, line_count):
		self.power_plot.cla()
		power=[a*b/1000 for a,b in zip(self.points[2],self.points[9])]
		self.power_plot.plot(self.points[0],power,'k')
		textstr = ''.join((("Latest: {}".format(round(power[-1],2)))))
		self.power_plot.text(0.03, 0.95, textstr, transform=self.power_plot.transAxes, fontsize=14, verticalalignment='top', bbox=self.props)
		self.power_plot.set_title("Power")
		self.power_plot.xaxis.set_visible(False)
		self.power_plot.grid()
		self.power_plot.set_ylim(0,160)

	def _graph_aux_bat_voltage(self, line_count):
		self.aux_bat_voltage_plot.cla()
		self.aux_bat_voltage_plot.plot(self.points[0],self.points[12],'c')
		textstr = '\n'.join((("Max: {}".format(self.edge_points[12][1])),("Min: {}".format(self.edge_points[12][0])), "Latest: {}".format(self.points[12][-1])))
		self.aux_bat_voltage_plot.text(0.03, 0.95, textstr, transform=self.aux_bat_voltage_plot.transAxes, fontsize=14, verticalalignment='top', bbox=self.props)
		self.aux_bat_voltage_plot.set_title("Aux Volt")
		self.aux_bat_voltage_plot.hlines(16.8, line_count-200, line_count, colors='g', linestyles='dashed', label='')
		self.aux_bat_voltage_plot.hlines(14.5, line_count-200, line_count, colors='y', linestyles='dashed', label='')
		self.aux_bat_voltage_plot.hlines(12, line_count-200, line_count, colors='r', linestyles='dashed', label='')
		self.aux_bat_voltage_plot.set_ylim(10,18)
		self.aux_bat_voltage_plot.grid()
		self.aux_bat_voltage_plot.xaxis.set_visible(False)

	def _graph_rpm(self, line_count):
		self.rpm_plot.cla()
		self.rpm_plot.plot(self.points[0],self.points[7],'c')
		wheelCir = 1.979 #in meters
		gearing= 55/14 #number of back sprocket teeth / front sprocket teeth
		curSpeed = round(float(self.points[7][-1])/60 *wheelCir / gearing*2.23694,2) #rpm/60*wheel circum/gearing   -> meters per second  convert meters per second to miles per hour
		maxSpeed = round(float(self.edge_points[7][-1])/60 *wheelCir / gearing*2.23694,2)
		textstr = '\n'.join((("Max RPM: {}".format(self.edge_points[7][1])),("Latest RPM: {}".format(self.points[7][-1])), ("Max MPH: {}".format(maxSpeed)), ("Latest MPH: {}".format(curSpeed))))
		self.rpm_plot.text(0.02, 0.95, textstr, transform=self.rpm_plot.transAxes, fontsize=14, verticalalignment='top', bbox=self.props)
		self.rpm_plot.set_title("Motor RPM")
		self.rpm_plot.xaxis.set_visible(False)
		self.rpm_plot.set_ylim(0,12000)
		self.rpm_plot.grid()
		self.rpm_plot.hlines(10000, line_count-200, line_count, colors='g', linestyles='dashed', label='')

	def _graph_torque(self, line_count):
		self.torque_plot.cla()
		self.torque_plot.plot(self.points[0],self.points[9],'k')
		self.torque_plot.plot(self.points[0],self.points[10],'g')
		textstr = '\n'.join((("Torque: {}".format(self.points[10][-1])),("Current: {}".format(self.points[9][-1]))))
		self.torque_plot.text(0.03, 0.95, textstr, transform=self.torque_plot.transAxes, fontsize=14, verticalalignment='top', bbox=self.props)
		self.torque_plot.set_title("Torque, Current")
		self.torque_plot.set_ylim(0,200)
		self.torque_plot.grid()
		self.torque_plot.xaxis.set_visible(False)


if __name__ == '__main__':
	grapher = XbeeDataGrapher()
	grapher.xbee_setup()
	grapher.graph_setup()
	mng = plt.get_current_fig_manager()
	mng.window.state('zoomed')
	plt.show()
	grapher.xbee_close()