import csv, sys
def main():
	inputfile = 'TriggerF032.csv'
	if len(sys.argv) >= 2:
		inputfile = str(sys.argv[1])
	with open(inputfile, mode='r') as csv_file:
		csv_reader = csv.DictReader(csv_file)
		line_count = 0
		for row in csv_reader:
			line_count += 1
		print(line_count)

if __name__ == "__main__":
   main()
