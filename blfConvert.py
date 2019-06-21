import can
import csv

filename = "TriggerF198"
log = can.BLFReader("{}.BLF".format(filename))
log = list(log)

log_output = []

for msg in log:
    msg = str(msg)
    log_output.append([msg[18:26],msg[38:40],msg[40:42],msg[46],msg[62],msg[67:90]])

with open("{}.csv".format(filename), "w", newline='') as f:
    writer = csv.writer(f,delimiter=',')
    writer.writerows(log_output)