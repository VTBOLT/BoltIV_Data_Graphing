import csv, sys, getopt
import matplotlib.pyplot as plt

def main(argv):
	points = [[]]      # points[index] contains and array of all points for that column
	edgePoints = [[float('inf'),float('-inf')]]  # edgepoint[index] will contain max at 1 and min at 0
	
	#read command line arguments and deal with errors
	try:
		opts, args = getopt.getopt(argv,"hp:q",["ifile="])
	except getopt.GetoptError:
		print('dataGrapher.py -[option]\n\t--prettyPrint\t-p <input file>\n\t--quickPrint\t-q\n')
		sys.exit(2)
	
	for opt, arg in opts:
		#deal with help text
		if opt == '-h':
			print('dataGrapher.py takes a csv and prints it to a graph. Default file is data.csv and default setting is pretty print.')
			print('dataGrapher.py -[option]\n\t--prettyPrint\t-p <input file>\n\t--quickPrint\t-q\n')
			sys.exit()
		#deal with pretty print
		elif opt in ("-p", "--prettyPrint"):
			inputfile = arg
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
				for i in range(len(head)-1):
					plt.figure(i+1)
					plt.plot(points[0],points[i+1],1)
					plt.title(head[i+1])
					plt.ylabel(head[i+1])
					plt.xlabel(head[0]);
					textstr = '\n'.join((("Max: {}".format(edgePoints[i+1][1])),("Min: {}".format(edgePoints[i+1][0])), "Latest: {}".format(points[i+1][-1])))
					props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
					plt.text(0.05, 0.95, textstr, transform=plt.subplot().transAxes, fontsize=14, verticalalignment='top', bbox=props)
				plt.autoscale(enable=True,axis='both',tight=None)
				plt.show()
		#deal with quick (realtime) print
		elif opt in ("-q", "--quickPrint"):
			points[0].append(input("enter x val: "))
			points[1].append(input("enter y val: "))
			plt.ion()
			plt.plot(points[0],points[1])
			plt.show()
			while 1:
				try:
					plt.plot(points[0],points[1])
					plt.autoscale()
					plt.draw()
					points[0].append(input("enter x val: "))
					points[1].append(input("enter y val: "))
				except KeyboardInterrupt:
					raise

#dont know what this does but we need it
if __name__ == "__main__":
   main(sys.argv[1:])