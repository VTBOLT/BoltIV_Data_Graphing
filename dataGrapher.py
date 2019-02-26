import csv, sys, getopt
import matplotlib.pyplot as plt

def main(argv):
	inputfile = 'data.csv'
	x = []
	y = []
	try:
		opts, args = getopt.getopt(argv,"hp:q:",["ifile="])
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
				for row in csv_reader:
					line_count += 1
					vary = float(row[head[1]])
					if vary > 0:
						x.append(float(row[head[0]]))
						y.append(vary)
				print('Processed {0} lines.'.format(line_count))
				plt.plot(x,y,1)
				plt.autoscale(enable=True,axis='both',tight=None)
				plt.show()
		elif opt in ("-q", "--quickPrint"):
			inputfile = arg
			quickParse(inputfile)
	print( 'Input file is ', inputfile)

if __name__ == "__main__":
   main(sys.argv[1:])