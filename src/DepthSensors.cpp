#include <ros/ros.h>
#include <sensor_msgs/Image.h>
#include <cv_bridge/cv_bridge.h>
#include <image_transport/image_transport.h>
#include <opencv2/opencv.hpp>
#include "turtlebot_gamepad_training_replay/DepthSensorValues.h"

class DepthScan
{
public:
	DepthScan()
	{
		ros::NodeHandle n;
		depth_sub = n.subscribe("camera/depth/image", 1, &DepthScan::depthCallback, this);
		depth_pub = n.advertise<turtlebot_gamepad_training_replay::DepthSensorValues>("DepthSensor", 1);
	}

	void depthCallback(const sensor_msgs::Image &img_msg){
		cv_bridge::CvImagePtr cv_ptr;
		turtlebot_gamepad_training_replay::DepthSensorValues d;
		int i, j;
		float depthvalues[640][480];
	
		try
		{
			cv_ptr = cv_bridge::toCvCopy(img_msg, sensor_msgs::image_encodings::TYPE_32FC1);
		}
		catch (cv_bridge::Exception& e)
		{
			ROS_ERROR("error");
			return;
		}
			
		cv::Mat depth(cv_ptr->image.rows, cv_ptr->image.cols, CV_32FC1);
		
		for (i = 0; i < cv_ptr->image.rows; i++) {
			float* Dimage = cv_ptr->image.ptr<float>(i);
			for (j = 0; j < cv_ptr->image.cols; j++) {
				depthvalues[i][j] = Dimage[j];
			}
		}
		ROS_INFO("depth : %d [m]", cv_ptr->image.rows);
		d.right_side = depthvalues[120][560];
		d.right_center = depthvalues[120][400];
		d.left_center = depthvalues[120][240];
		d.left_side = depthvalues[120][80];
		d.sum_center = d.left_center + d.right_center;
		d.sum_all = d.sum_center + d.left_side + d.right_side;
		
		depth_pub.publish(d);
	}
private:
	ros::Subscriber depth_sub;
	ros::Publisher depth_pub;
};

int main(int argc, char **argv){
	ros::init(argc, argv, "DepthSensors");
	DepthScan DepthSensors;
	ros::spin();
}

