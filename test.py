import csv, sys, getopt
import matplotlib.pyplot as plt

def main(argv):
	points = [[]]      # points[index] contains and array of all points for that column
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
		for row in csv_reader:
			line_count += 1
			for i in range(len(head)):
				points[i].append(float(row[head[i]]))
				if float(row[head[i]]) < edgePoints[i][0]:
					edgePoints[i][0] = float(row[head[i]])
				if float(row[head[i]]) > edgePoints[i][1]:
					edgePoints[i][1] = float(row[head[i]])
		print('Processed {0} lines.'.format(line_count))
		
		ax1=plt.subplot(313)
		ax1.plot(points[0],points[9],'k')
		ax1.set_title(head[9])
		textstr = '\n'.join((("Max: {}".format(edgePoints[9][1])),("Min: {}".format(edgePoints[9][0])), "Latest: {}".format(points[9][-1])))
		props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
		ax1.text(0.05, 0.95, textstr, transform=ax1.transAxes, fontsize=14, verticalalignment='top', bbox=props)
		
		ax2=plt.subplot(321)
		ax2.plot(points[0],points[2],'g')
		ax2.set_title(head[2])
		textstr = '\n'.join((("Max: {}".format(edgePoints[2][1])),("Min: {}".format(edgePoints[2][0])), "Latest: {}".format(points[2][-1])))
		ax2.text(0.05, 0.95, textstr, transform=ax2.transAxes, fontsize=14, verticalalignment='top', bbox=props)
		
		ax3=plt.subplot(322)
		ax3.plot(points[0],points[3],'r')
		ax3.plot(points[0],points[4],'b')
		ax3.set_title("Min/Max Cell Temps")
		textstr = '\n'.join((("Max: {}".format(edgePoints[3][1])),("Min: {}".format(edgePoints[3][0])), "Latest: {}".format(points[3][-1])))
		ax3.text(0.05, 0.95, textstr, transform=ax3.transAxes, fontsize=14, verticalalignment='top', bbox=props)
		
		ax4=plt.subplot(323)
		ax4.plot(points[0],points[5],'r')
		ax4.plot(points[0],points[6],'b')
		ax4.set_title("Min/Max Cell Volts")
		textstr = '\n'.join((("Max: {}".format(edgePoints[5][1])),("Min: {}".format(edgePoints[5][0])), "Latest: {}".format(points[5][-1])))
		ax4.text(0.05, 0.95, textstr, transform=ax4.transAxes, fontsize=14, verticalalignment='top', bbox=props)
		
		ax5=plt.subplot(324)
		ax5.plot(points[0],points[7],'c')
		ax5.plot(points[0],points[8],'m')
		ax5.set_title("Aux Volt and Pump Volt")
		textstr = '\n'.join((("Max: {}".format(edgePoints[7][1])),("Min: {}".format(edgePoints[7][0])), "Latest: {}".format(points[7][-1])))
		ax5.text(0.05, 0.95, textstr, transform=ax5.transAxes, fontsize=14, verticalalignment='top', bbox=props)
		
		plt.autoscale(enable=True,axis='both',tight=None)
		plt.show()
if __name__ == "__main__":
   main(sys.argv[1:])