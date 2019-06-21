import csv
import matplotlib.pyplot as plt
import math
import sys
from progress.bar import IncrementalBar
graphNumbers=[0,15,13,4,3,5,6,82,89,57,22,14]
power = []
def main():
	points = [[]]  # points[index] contains and array of all points for that column
	inputfile = 'TriggerF032.csv'
	numberOfLines =3248693
	if len(sys.argv) >= 2:
		inputfile = str(sys.argv[1])
		if len(sys.argv) == 3:
			numberOfLines = int(sys.argv[2])
	with open(inputfile, mode='r') as csv_file:
		csv_reader = csv.DictReader(csv_file)
		line_count = 1
		firstLine=next(csv_reader)
		head = [row for row in firstLine]
		i=0
		for row in head:
			points.append([])
			# print(("{} "+row).format(i))
			i+=1
		with IncrementalBar('\tProcessing', max=100) as bar:
			for row in csv_reader:
				line_count += 1
				if line_count %(math.ceil(numberOfLines/100)) == 0:
					bar.next()
				for i in range(len(head)):
					if i in graphNumbers:
						if(points[0][i]< 76000 and i!=graphNumbers[1] and i!=graphNumbers[2] and i!=graphNumbers[5] and i!=graphNumbers[6] and i!=graphNumbers[7] and i!=graphNumbers[8]) or (float(row[head[i]]) >= 2):
							points[i].append(float(row[head[i]]))
							
			global power
			power=[a*b/1000 for a,b in zip(points[graphNumbers[2]],points[graphNumbers[10]])]
			bar.next()

		props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
		fig=plt.figure()
		ax1=fig.add_subplot(3,3,7)#SOC
		ax2=fig.add_subplot(3,3,2)#FPV
		ax3=fig.add_subplot(3,3,3)#TEMP
		ax4=fig.add_subplot(3,3,9)#Volt
		ax5=fig.add_subplot(3,3,8)#Motor/MC temp
		ax6=fig.add_subplot(3,2,3)#Power
		ax8=fig.add_subplot(3,2,4)#RPM
		ax9=fig.add_subplot(3,3,1)#Torque, Current
		plt.ion()
		mng = plt.get_current_fig_manager()
		mng.window.state('zoomed')
		plt.show()
		
		ax1.plot(points[graphNumbers[1]],'k')
		ax1.set_title(head[graphNumbers[1]][head[graphNumbers[1]].rindex(':')+1:].replace("_", " "))
		ax1.set_ylim([0,100])
		ax1.grid()
		ax1.xaxis.set_visible(False)
		ax1.hlines(95, 0, line_count, colors='g', linestyles='dashed', label='')
		ax1.hlines(30, 0, line_count, colors='y', linestyles='dashed', label='')
		ax1.hlines(15, 0, line_count, colors='r', linestyles='dashed', label='')
		
		ax2.plot(points[graphNumbers[2]],'g')
		ax2.set_title(head[graphNumbers[2]][head[graphNumbers[2]].rindex(':')+1:].replace("_", " "))
		ax2.set_ylim((450,750))
		ax2.grid()
		ax2.xaxis.set_visible(False)
		ax2.hlines(698, 0, line_count, colors='b', linestyles='dashed', label='')
		ax2.hlines(597, 0, line_count, colors='k', linestyles='dashed', label='')
		ax2.hlines(480, 0, line_count, colors='r', linestyles='dashed', label='')
		
		ax3.plot(points[graphNumbers[3]],'r')
		ax3.plot(points[graphNumbers[4]],'b')
		ax3.set_title("Cell Temps")
		ax3.xaxis.set_visible(False)
		ax3.set_ylim(20,90)
		ax3.grid()
		textstr = '\n'.join((("Max Temp:{}C".format(max(points[graphNumbers[3]])),("Min Temp:{}C".format(min(points[graphNumbers[4]]))))))
		ax3.text(0.02, 0.95, textstr, transform=ax3.transAxes, fontsize=14, verticalalignment='top', bbox=props)
		ax3.hlines(40, 0, line_count, colors='g', linestyles='dashed', label='')
		ax3.hlines(60, 0, line_count, colors='y', linestyles='dashed', label='')
		ax3.hlines(80, 0, line_count, colors='r', linestyles='dashed', label='')
		
		ax4.plot(points[graphNumbers[5]],'r')
		ax4.plot(points[graphNumbers[6]],'b')
		ax4.set_title("Min/Max Cell Volts")
		ax4.xaxis.set_visible(False)
		ax4.grid()
		ax4.set_ylim(2.5,4.5)
		textstr = '\n'.join((("Max Volt:{}V".format(max(points[graphNumbers[5]])),("Min Volt:{}V".format(min(points[graphNumbers[6]]))))))
		ax4.text(0.02, 0.1, textstr, transform=ax4.transAxes, fontsize=14, verticalalignment='top', bbox=props)
		ax4.hlines(4.2, 0, line_count, colors='g', linestyles='dashed', label='')
		ax4.hlines(3.8, 0, line_count, colors='y', linestyles='dashed', label='')
		ax4.hlines(3.0, 0, line_count, colors='r', linestyles='dashed', label='')
		
		ax5.plot(points[graphNumbers[7]],'k')
		ax5.plot(points[graphNumbers[8]],'b')
		ax5.set_title("Motor/ Motor Controller Temp")
		ax5.xaxis.set_visible(False)
		ax5.grid()
		ax5.set_ylim(20,180)
		textstr = '\n'.join((("Max Motor Temp:{}C".format(max(points[graphNumbers[7]])),"Max Motor Controller Temp:{}C".format(max(points[graphNumbers[8]])))))
		ax5.text(0.02, 0.95, textstr, transform=ax5.transAxes, fontsize=14, verticalalignment='top', bbox=props)
		ax5.hlines(80, 0, line_count, colors='y', linestyles='dashed', label='')
		ax5.hlines(100, 0, line_count, colors='r', linestyles='dashed', label='')
		ax5.hlines(170, 0, line_count, colors='r', linestyles='dashed', label='')
		
		ax6.plot(power,'r')
		ax6.set_title("Power")
		ax6.xaxis.set_visible(False)
		ax6.grid()
		textstr = "Max Power:{}Nm".format(round(max(power)),3)
		ax6.text(0.02, 0.95, textstr, transform=ax6.transAxes, fontsize=14, verticalalignment='top', bbox=props)
		ax6.set_ylim(0,160)
		
		ax8.plot(points[graphNumbers[9]],'c')
		ax8.set_title(head[graphNumbers[9]][head[graphNumbers[9]].rindex(':')+1:].replace("_", " "))
		ymax = max(points[graphNumbers[9]])
		xpos = points[graphNumbers[9]].index(ymax)
		xmax = points[0][xpos]
		wheelCir = 1.979
		gearing= 55/14
		maxSpeed = round(float(ymax)/60 *wheelCir / gearing*2.23694,2)
		textstr = '\n'.join((("Max Speed:{}RPM".format(ymax),("Max Speed:{}MPH".format(maxSpeed)))))
		ax8.text(0.02, 0.95, textstr, transform=ax8.transAxes, fontsize=14, verticalalignment='top', bbox=props)
		ax8.xaxis.set_visible(False)
		ax8.set_ylim(0,12000)
		ax8.grid()
		ax8.hlines(10000, 0, line_count, colors='g', linestyles='dashed', label='')
		
		ax9.plot(points[graphNumbers[10]],'g')
		ax9.plot(points[graphNumbers[11]],'k')
		ax9.set_title("Torque, Current")
		ymax = max(points[graphNumbers[10]])
		xpos = points[graphNumbers[10]].index(ymax)
		xmax = points[0][xpos]
		textstr = '\n'.join((("Max Torque:{}Nm".format(ymax),("Max Current:{}A".format(max(points[graphNumbers[11]]))))))
		ax9.text(0.02, 0.95, textstr, transform=ax9.transAxes, fontsize=14, verticalalignment='top', bbox=props)
		ax9.set_ylim(0,200)
		ax9.grid()
		ax9.xaxis.set_visible(False)
				
		plt.draw()
		plt.pause(0.00000000001)

		print('\nProcessed {0} lines.'.format(line_count))
		input("press enter to close graph")
if __name__ == "__main__":
   main()
