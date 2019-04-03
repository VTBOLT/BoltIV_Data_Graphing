import csv
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def main():
	points = [[]]  # points[index] contains and array of all points for that column
	inputfile = 'data3.csv'
	with open(inputfile, mode='r') as csv_file:
		csv_reader = csv.DictReader(csv_file)
		line_count = 1
		firstLine=next(csv_reader)
		head = [row for row in firstLine]
		for row in head:
			points.append([])
		
		props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
		ax1=plt.subplot(111,projection='3d')
		
		plt.ion()
		plt.show()
		
		for row in csv_reader:
			ax1.cla()
			line_count += 1
			for i in range(len(head)):
				points[i].append(float(row[head[i]]))
				
			if line_count<50:
				ax1.plot(points[0],points[1],points[2])
			else:
				ax1.plot(points[0][line_count-50:-1],points[1][line_count-50:-1],points[2][line_count-50:-1])
				
			textstr = '\n'.join((("X:{}".format(points[0][-1])),("Y:{}".format(points[1][-1])), "Z:{}".format(points[2][-1])))
			ax1.text(0.05, 0.95, 0.05, textstr, transform=ax1.transAxes, fontsize=14, verticalalignment='top', bbox=props)
			ax1.set_title('3d plot')
			ax1.set_xlim(-2,2)
			ax1.set_ylim(-2,2)
			ax1.set_zlim(-2,2)
			ax1.xaxis._axinfo['jugled'] = (0,0,0)
			ax1.spines['right'].set_position('zero')
			
			plt.draw()
			plt.pause(0.0001)

		input("press enter to close graph")
		print('Processed {0} lines.'.format(line_count))
if __name__ == "__main__":
   main()
