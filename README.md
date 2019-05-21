# BoltIV Data Graphing
Program for graphing CAN data from the XBEEs.

3 important files:

xbeeDataGraphing.py opens a graphing window and waits for data from the xbee and graphs it as it comes in
syntax:> py xbeeDataGrapher.py

xbeeRec.py prints all raw xbee data to the terminal, no graphing
syntax:> py xbeeRec.py

graphCSV.py graphs data from a csv. The csv should be the one that we get from CANalyzer.
syntax:> graphCSV.py *filename*
