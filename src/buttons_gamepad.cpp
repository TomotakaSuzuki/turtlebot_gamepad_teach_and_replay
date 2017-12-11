#include "ros/ros.h"
#include <ros/package.h>
#include "sensor_msgs/Joy.h"
#include "turtlebot_gamepad_training_replay/ButtonValues.h"
#include <fstream>
using namespace ros;

bool training = false;
bool replay = false;

void joyCallback(const sensor_msgs::Joy::ConstPtr& msg)
{
    if (msg->buttons[5] == 1 && msg->buttons[4] == 0) {
        training = true;
    } else if (msg->buttons[5] == 0 && msg->buttons[4] == 0) {
        training = false;
    }
    if (msg->buttons[5] == 0 && msg->buttons[4] == 1) {
        replay = true;
    } else if (msg->buttons[5] == 0 && msg->buttons[4] == 0) {
        replay = false;
    }
}

int main(int argc, char **argv)
{
    init(argc, argv, "buttons");
    NodeHandle n;

    Subscriber sub = n.subscribe("joy", 1, joyCallback);
    Publisher pub = n.advertise<turtlebot_gamepad_training_replay::ButtonValues>("buttons", 5);

    ros::Rate loop_rate(10);
    turtlebot_gamepad_training_replay::ButtonValues msg;
    int c[2] = {0, 0};
    while (ok()) {
        msg.training_fg = training;
        msg.replay_fg = replay;

        c[0] = msg.training_fg ? 1+c[0] : 0;
        c[1] = msg.replay_fg ? 1+c[1] : 0;
        
        if (c[0] > 4) {
            msg.training = not msg.training;
            c[0] = 0;
        }
        if (c[1] > 4) {
            msg.replay = not msg.replay;
            c[1] = 0;
        }

        pub.publish(msg);
        spinOnce();
        loop_rate.sleep();
    }
    exit(0);
}
