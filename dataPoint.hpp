#pragma once
class dataPoint
{
public:
	dataPoint();
	~dataPoint();
	dataPoint(double timeIn, double dataIn) { time = timeIn; data = dataIn; }
	double setTime(double timeIn) { time = timeIn; }
	double setData(double dataIn) { data = dataIn; }
	double getTime() { return time; }
	double getData() { return data; }

private:
	double time;
	double data;
};