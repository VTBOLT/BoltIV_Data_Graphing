import csv
from digi.xbee.devices import XBeeDevice
PORT = "COM7"
BAUD_RATE = 57600

def main():
    print(" +-----------------------------------------+")
    print(" | XBee Python Library Send Data Sample |")
    print(" +-----------------------------------------+\n")

    device = XBeeDevice(PORT, BAUD_RATE)

    try:
        device.open()
        inputfile = 'data2.csv'
        with open(inputfile, mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            firstLine=next(csv_reader)
            head = [row for row in firstLine]
            line_count = 1
            for row in csv_reader:
                line_count+=1
                send = "({0},{1},{2},{3},{4},{5},{6},{7},{8},{9})".format(row[head[0]],row[head[1]],row[head[2]],row[head[3]],row[head[4]],row[head[5]],row[head[6]],row[head[7]],row[head[8]],row[head[9]])
                device.send_data_broadcast(send)
                #print(line_count, end=",", flush=True)
    finally:
        if device is not None and device.is_open():
            device.close()
            print ("Sent {} lines".format(line_count))

if __name__ == '__main__':
    main()