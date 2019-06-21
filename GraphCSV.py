import csv
import matplotlib.pyplot as plt
graphNumbers=[82, 22, 57]
def main():
	points = [[]]  # points[index] contains and array of all points for that column
	inputfile = 'TriggerF032.csv'
	with open(inputfile, mode='r') as csv_file:
		csv_reader = csv.DictReader(csv_file)
		line_count = 1
		firstLine=next(csv_reader)
		head = [row for row in firstLine]
		i=0
		for row in head:
			points.append([])
			print(("{} "+row).format(i))
			i+=1
		for row in csv_reader:
			line_count += 1
			if line_count %10000 == 0:
				percent = line_count/3248693*100
				print("{}%".format('%.3f'%percent))
			for i in range(len(head)):
				if i==0 or i==graphNumbers[0] or i==graphNumbers[1] or i==graphNumbers[2]:
					points[i].append(float(row[head[i]]))
					
		props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
		ax1=plt.subplot(311)
		ax2=plt.subplot(312)
		ax3=plt.subplot(313)
		plt.ion()
		plt.show()
		ax1.set_title(head[graphNumbers[0]][head[graphNumbers[0]].rindex(':')+1:].replace("_", " "))
		ax1.plot(points[0],points[graphNumbers[0]],'k')#torque commanded
		ax2.set_title(head[graphNumbers[1]][head[graphNumbers[1]].rindex(':')+1:].replace("_", " "))
		ax2.plot(points[0],points[graphNumbers[1]],'k')#pack current
		ax3.set_title(head[graphNumbers[2]][head[graphNumbers[2]].rindex(':')+1:].replace("_", " "))
		ax3.plot(points[0],points[graphNumbers[2]],'k')#motor speed
		plt.draw()
		plt.pause(0.00000000001)
			# ax1.plot(points[0],points[4],'b')
			# ax1.plot(points[0],points[5],'r')
			# ax1.plot(points[0],points[6],'b')
			# ax1.plot(points[0],points[7],'c')
			# ax1.plot(points[0],points[8],'m')
			
			

		input("press enter to close graph")
		print('Processed {0} lines.'.format(line_count))
if __name__ == "__main__":
   main()
