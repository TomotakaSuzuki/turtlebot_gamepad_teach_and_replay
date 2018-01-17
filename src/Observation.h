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
	Observation(float left_s, float left_m, float left_c, float right_c, float right_m, float right_s);

	void setValues(float left_s, float left_m, float left_c, float right_c, float right_m, float right_s);

	float ls;
    float lm;
	float lc;
	float rc;
    float rm;
	float rs;
	double log_ls;
    double log_lm;
	double log_lc;
	double log_rc;
    double log_rm;
	double log_rs;
};

#endif
