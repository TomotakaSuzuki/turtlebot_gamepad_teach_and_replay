#include "Observation.h"
#include <iostream>
#include <string>
#include <cmath>

Observation::Observation()
{
}

Observation::Observation(float left_s,float left_c, float right_c, float right_s)
{
	setValues(left_s,left_c,right_c,right_s);
}

void Observation::setValues(float left_s,float left_c, float right_c, float right_s)
{
	ls = left_s > 0 ? left_s : 1;
	lc = left_c > 0 ? left_c : 1;
	rc = right_c > 0 ? right_c : 1;
	rs = right_s > 0 ? right_s : 1;

	log_ls = log10((double)ls);
	log_lc = log10((double)lc);
	log_rc = log10((double)rc);
	log_rs = log10((double)rs);
}
