#!/usr/bin/env python
# Copyright 2017 Tomotaka Suzuki
# Released under the BSD License.
import rospy
from sensor_msgs.msg import Joy
from turtlebot_gamepad_training_replay.msg import ButtonValues

class Buttons(object):
    def __init__(self):
        self._joy_sub = rospy.Subscriber('/joy', Joy, self.joy_callback, queue_size=1)
        self._btm_pub = rospy.Publisher('/buttons', ButtonValues, queue_size=1)
        self.count = 2 
        self.training = False
        self.replay = False

    def counter(self, c):
        if c <= 0: return 1
        if c >= 11: return 10
        return c

    def joy_callback(self, joy_msg):
        b = ButtonValues()
        if joy_msg.buttons[5] == 1: self.count += 1 
        if joy_msg.buttons[4] == 1: self.count -= 1
        self.count = self.counter(self.count)

        if self.count == 10: b.training = True
        else: b.training = False
        if self.count == 1: b.replay = True
        else: b.replay = False

        self._btm_pub.publish(b)

if __name__ == '__main__':
    rospy.init_node('control_buttons', anonymous=True)
    button_control = Buttons()
    rospy.spin()
