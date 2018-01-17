#!/usr/bin/env python
# Copyright 2017 Masahiro Kato
# Copyright 2017 Ryuichi Ueda
# Released under the BSD License.

import rospy, rosbag, rosparam
import math, sys, random, datetime
from std_srvs.srv import Trigger, TriggerResponse
from geometry_msgs.msg import Twist
from turtlebot_gamepad_training_replay.msg import Event, DepthSensorValues, ButtonValues

class Logger():
    def __init__(self):
        self.depth_values = DepthSensorValues()
        self.cmd_vel = Twist()
        
        self._decision = rospy.Publisher('/event', Event, queue_size=100)
 
        rospy.Subscriber('/buttons', ButtonValues, self.button_callback, queue_size=1)
        rospy.Subscriber('/DepthSensor', DepthSensorValues, self.sensor_callback)
        rospy.Subscriber('/cmd_vel_mux/input/teleop', Twist, self.cmdvel_callback)

        self.on = False 
        self.bag_open = False

    def button_callback(self, btm_msg):
        self.on = btm_msg.training

    def sensor_callback(self, messages):
        self.depth_values = messages
    
    def cmdvel_callback(self, messages):
        self.cmd_vel = messages 

    def output_decision(self):
        if not self.on:
            if self.bag_open:
                self.bag.close()
                self.bag_open = False
                print("Training Stop.")
            return
        else:
            if not self.bag_open:
                filename = datetime.datetime.today().strftime("%Y%m%d_%H%M%S") + '.bag'
                rosparam.set_param("/current_bag_file", filename)
                self.bag = rosbag.Bag(filename, 'w')
                self.bag_open = True
                print("Training Start.")
            
        s = self.depth_values
        a = self.cmd_vel
        e = Event()

        e.right_side = s.right_side
        e.right_middle = s.right_middle
        e.right_center = s.right_center
        e.left_center = s.left_center
        e.left_middle = s.left_middle
        e.left_side = s.left_side
        e.linear_x = a.linear.x
        e.angular_z = a.angular.z

        self._decision.publish(e)
        self.bag.write('/event', e)

    def run(self):
        rate = rospy.Rate(10)
        data = Twist()

        while not rospy.is_shutdown():
            self.output_decision()
            rate.sleep()

if __name__ == '__main__':
    rospy.init_node('turtlebot_logger')
    Logger().run()
