#include <vector>
#include <string>
#include <cstdlib>
#include "dataPoint.hpp"

class dataGrapher
{
public:
	dataGrapher();
	~dataGrapher();
	std::vector<dataPoint> prettyParse(std::string infile);
	std::vector<dataPoint> quickParse(std::string infile);

private:
	std::vector<dataPoint> list;
};
int main(int argc, char** argv)
{
	dataGrapher();
}
dataGrapher::dataGrapher()
{
	
}

dataGrapher::~dataGrapher()
{
}

std::vector<dataPoint> dataGrapher::prettyParse(std::string infile)
{
	
}
std::vector<dataPoint> dataGrapher::quickParse(std::string infile)
{
	
}