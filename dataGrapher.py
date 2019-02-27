import csv, sys, getopt
import matplotlib.pyplot as plt

def main(argv):
	points = [[]]
	try:
		opts, args = getopt.getopt(argv,"hp:q",["ifile="])
	except getopt.GetoptError:
		print('dataGrapher.py -[option]\n\t--prettyPrint\t-p <input file>\n\t--quickPrint\t-q <input stream>\t')
		sys.exit(2)
	for opt, arg in opts:
		if opt == '-h':
			print('dataGrapher.py takes a csv and prints it to a graph. Default file is data.csv and default setting is pretty print.')
			print('dataGrapher.py -[option]\n\t--prettyPrint\t-p <input file>\n\t--quickPrint\t-q <input stream>\t')
			sys.exit()
		elif opt in ("-p", "--prettyPrint"):
			inputfile = arg
			with open(inputfile, mode='r') as csv_file:
				csv_reader = csv.DictReader(csv_file)
				line_count = 1
				firstLine=next(csv_reader)
				head = [row for row in firstLine]
				for row in head:
					points.append([])
				for row in csv_reader:
					line_count += 1
					for i in range(len(head)):
						points[i].append(float(row[head[i]]))
				print('Processed {0} lines.'.format(line_count))
				for i in range(len(head)-1):
					plt.figure(i+1)
					plt.plot(points[0],points[i+1],1)
				plt.autoscale(enable=True,axis='both',tight=None)
				plt.show()
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
	print( 'Input file is ', inputfile)

if __name__ == "__main__":
   main(sys.argv[1:])