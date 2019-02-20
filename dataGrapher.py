import csv, sys, getopt
import matplotlib.pyplot as plt

def main(argv):
	inputfile = 'data.csv'
	x = []
	y = []
	try:
		opts, args = getopt.getopt(argv,"hp:q:",["ifile="])
	except getopt.GetoptError:
		print('dataGrapher.py -[option]\n-p <inputfile>\t--prettyPrint\n-q <inputStream>\t--quickPrint')
		sys.exit(2)
	for opt, arg in opts:
		if opt == '-h':
			print('dataGrapher.py -[option]\n-p <inputfile>\t--prettyPrint\n-q <inputStream>\t--quickPrint')
			sys.exit()
		elif opt in ("-p", "--prettyPrint"):
			inputfile = arg
			with open(inputfile, mode='r') as csv_file:
				csv_reader = csv.DictReader(csv_file)
				line_count = 0
				for row in csv_reader:
					if line_count == 0:
						print('Column names are {0}'.format(", ".join(row)))
						line_count += 1
						vary = float(row["BOLT3_New_Param::M165_Motor_Position_Info::D2_Motor_Speed"])
						if vary > 0:
							x.append(float(row["Time [s]"]))
							y.append(vary)
							line_count += 1
				print('Processed {0} lines.'.format(line_count))
				plt.scatter(x,y)
				plt.show()
		elif opt in ("-q", "--quickPrint"):
			inputfile = arg
			quickParse(inputfile)
	print( 'Input file is ', inputfile)

if __name__ == "__main__":
   main(sys.argv[1:])