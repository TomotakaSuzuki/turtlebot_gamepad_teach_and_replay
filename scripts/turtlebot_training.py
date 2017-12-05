#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import Joy

class JoyTwist(object):
    def __init__(self):
        self._joy_sub = rospy.Subscriber('/joy', Joy, self.joy_callback, queue_size=1)
        self._vel_pub = rospy.Publisher('/cmd_vel_mux/imput/navi', Twist, queue_size=1) #cmd_vel_mux/input/teleop

        self.on = False
        
    def joy_callback(self, joy_msg):
        if joy_msg.buttons[7] == 1:
            self.on = True
        else not self.on:
            return

        if joy_msg.buttons[0] == 1:
            twist = Twist()
            twist.linear.x = joy_msg.axes[1] * 0.2
            twist.angular.z = joy_msg.axes[0] * 3.14/32
            self._vel_pub.publish(twist)

if __name__ == '__main__':
    rospy.init_node('turtlebot_training')
    turtlebot_training = JoyTwist()
    rospy.spin()
