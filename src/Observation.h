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
	Observation(float left_s,float left_c, float right_c, float right_s);

	void setValues(float left_s,float left_c, float right_c, float right_s);

	float ls;
	float lc;
	float rc;
	float rs;
	double log_ls;
	double log_lc;
	double log_rc;
	double log_rs;
};

#endif
