#!/usr/bin/env python
# Copyright 2017 Ryo Okazaki
# Copyright 2017 Ryuichi Ueda
# Copyright 2017 Tomotaka Suzuki
# Released under the BSD License

import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import Joy
from turtlebot_gamepad_training_replay.msg import ButtonValues

class JoyTwist(object):
    def __init__(self):
        self._btm_sub = rospy.Subscriber('/buttons', ButtonValues, self.button_callback, queue_size=1)
        self._joy_sub = rospy.Subscriber('/joy', Joy, self.joy_callback, queue_size=1)
        self._vel_pub = rospy.Publisher('/cmd_vel_mux/input/teleop', Twist, queue_size=1)

        self.level = 1
        self.on = False

    def limitter(self, lvl):
        if lvl <= 0: return 1
        if lvl >= 6: return 5
        return lvl
       
    def button_callback(self, btm_msg):
        self.on = btm_msg.training 

    def joy_callback(self, joy_msg):
        if not self.on:
            return

        if joy_msg.buttons[7] == 1: self.level += 1
        if joy_msg.buttons[6] == 1: self.level -= 1
        self.level = self.limitter(self.level)

        if joy_msg.buttons[0] == 1:
            twist = Twist()
            twist.linear.x = joy_msg.axes[1] * 0.2 * self.level
            twist.angular.z = joy_msg.axes[0] * 3.14/32 * (self.level + 15)
            self._vel_pub.publish(twist)

        if joy_msg.axes[1] == joy_msg.axes[0] == 0:
            self.level -= 1

if __name__ == '__main__':
    rospy.init_node('turtlebot_training')
    turtlebot_training = JoyTwist()
    rospy.spin()
