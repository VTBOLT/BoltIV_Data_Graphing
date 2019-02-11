#pragma once
#include <vector>
#include <cstdlib>
#include "dataPoint.hpp"

class dataGrapher
{
public:
	dataGrapher();
	~dataGrapher();

private:
	std::vector<dataPoint> dataVector;
};