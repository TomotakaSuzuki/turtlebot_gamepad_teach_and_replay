#ifndef __PF_H__
#define __PF_H__

#include <vector>
#include "Particle.h"
#include "ProbDistribution.h"
#include "turtlebot_gamepad_training_replay/PFoEOutput.h"
using namespace ros;

class Episodes;
class Observation;
class Action;

class ParticleFilter
{
public:
	ParticleFilter(int num, Episodes *ep);
	void init(void);
	void print(void);

//	Action sensorUpdate(Observation *obs, Episodes *ep, turtlebot_gamepad_training_replay::PFoEOutput *out);
	Action sensorUpdate(Observation *obs, Action *act, Episodes *ep, turtlebot_gamepad_training_replay::PFoEOutput *out);
	Action mode(Episodes *ep);
	Action modeParticle(Episodes *ep);
	Action average(Episodes *ep);
	void motionUpdate(Episodes *ep);
private:
	vector<Particle> particles;
	ProbDistributions prob;

	Episodes *episodes;

	double likelihood(Observation *past, Observation *last);
	double likelihood(Observation *past, Observation *last, Action *past_a, Action *last_a);

	void resampling(vector<Particle> *ps);
	void normalize(void);
};

#endif
