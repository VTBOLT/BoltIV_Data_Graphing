import csv
import matplotlib.pyplot as plt

def main():
	points = [[]]  # points[index] contains and array of all points for that column
	edgePoints = [[float('inf'),float('-inf')]]  # edgepoint[index] will contain max at 1 and min at 0
	inputfile = 'data2.csv'
	with open(inputfile, mode='r') as csv_file:
		csv_reader = csv.DictReader(csv_file)
		line_count = 1
		firstLine=next(csv_reader)
		head = [row for row in firstLine]
		for row in head:
			points.append([])
			edges = [float('inf'),float('-inf')]
			edgePoints.append(edges)
		
		props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
		ax1=plt.subplot(313)
		ax2=plt.subplot(321)
		ax3=plt.subplot(322)
		ax4=plt.subplot(323)
		ax5=plt.subplot(324)
		plt.ion()
		plt.show()
		
		for row in csv_reader:
			ax1.cla()
			ax2.cla()
			ax3.cla()
			ax4.cla()
			ax5.cla()
			line_count += 1
			for i in range(len(head)):
				points[i].append(float(row[head[i]]))
				if float(row[head[i]]) < edgePoints[i][0]:
					edgePoints[i][0] = float(row[head[i]])
				if float(row[head[i]]) > edgePoints[i][1]:
					edgePoints[i][1] = float(row[head[i]])
			if line_count<100:
				ax1.plot(points[0],points[9],'k')
				ax2.plot(points[0],points[2],'g')
				ax3.plot(points[0],points[3],'r')
				ax3.plot(points[0],points[4],'b')
				ax4.plot(points[0],points[5],'r')
				ax4.plot(points[0],points[6],'b')
				ax5.plot(points[0],points[7],'c')
				ax5.plot(points[0],points[8],'m')
			else:
				ax1.plot(points[0][line_count-100:-1],points[9][line_count-100:-1],'k')
				ax2.plot(points[0][line_count-100:-1],points[2][line_count-100:-1],'g')
				ax3.plot(points[0][line_count-100:-1],points[3][line_count-100:-1],'r')
				ax3.plot(points[0][line_count-100:-1],points[4][line_count-100:-1],'b')
				ax4.plot(points[0][line_count-100:-1],points[5][line_count-100:-1],'r')
				ax4.plot(points[0][line_count-100:-1],points[6][line_count-100:-1],'b')
				ax5.plot(points[0][line_count-100:-1],points[7][line_count-100:-1],'c')
				ax5.plot(points[0][line_count-100:-1],points[8][line_count-100:-1],'m')
				
			textstr = '\n'.join((("Max: {}".format(edgePoints[9][1])),("Min: {}".format(edgePoints[9][0])), "Latest: {}".format(points[9][-1])))
			ax1.text(0.05, 0.95, textstr, transform=ax1.transAxes, fontsize=14, verticalalignment='top', bbox=props)
			ax1.set_title(head[9])
			textstr = '\n'.join((("Max: {}".format(edgePoints[2][1])),("Min: {}".format(edgePoints[2][0])), "Latest: {}".format(points[2][-1])))
			ax2.text(0.05, 0.95, textstr, transform=ax2.transAxes, fontsize=14, verticalalignment='top', bbox=props)
			ax2.set_title(head[2])
			textstr = '\n'.join((("Max: {}".format(edgePoints[3][1])),("Min: {}".format(edgePoints[3][0])), "Latest: {}".format(points[3][-1])))
			ax3.text(0.05, 0.95, textstr, transform=ax3.transAxes, fontsize=14, verticalalignment='top', bbox=props)
			ax3.set_title("Min/Max Cell Temps")
			textstr = '\n'.join((("Max: {}".format(edgePoints[5][1])),("Min: {}".format(edgePoints[5][0])), "Latest: {}".format(points[5][-1])))
			ax4.set_title("Min/Max Cell Volts")
			ax4.text(0.05, 0.95, textstr, transform=ax4.transAxes, fontsize=14, verticalalignment='top', bbox=props)
			textstr = '\n'.join((("Max: {}".format(edgePoints[7][1])),("Min: {}".format(edgePoints[7][0])), "Latest: {}".format(points[7][-1])))
			ax5.text(0.05, 0.95, textstr, transform=ax5.transAxes, fontsize=14, verticalalignment='top', bbox=props)
			ax5.set_title("Aux Volt and Pump Volt")
			
			plt.draw()
			plt.pause(0.0001)

		input("press enter to close graph")
		print('Processed {0} lines.'.format(line_count))
if __name__ == "__main__":
   main()