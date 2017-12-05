#ifndef __OBS_H_ 
#define __OBS_H_

#include <string>
#include <vector>
#include <fstream>
#include "ros/ros.h"
using namespace std;

class Observation{
public:
	Observation();
	Observation(int left_s,int left_c, int right_c, int right_s);

	void setValues(int left_s,int left_c, int right_c, int right_s);

	int ls;
	int lc;
	int rc;
	int rs;
	double log_ls;
	double log_lc;
	double log_rc;
	double log_rs;
};

#endif
