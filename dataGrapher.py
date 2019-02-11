import csv

with open('data2.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print('Column names are {0}'.format(", ".join(row)))
            line_count += 1
        print('\tTime:{0} Speed:{1}.'.format(row["Time"],row["Motor Speed"]))
        line_count += 1
    print('Processed {0} lines.'.format(line_count))