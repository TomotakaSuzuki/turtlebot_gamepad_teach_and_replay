#!/usr/bin/env python
import rospy
from sensor_msgs.msg import Joy
from turtlebot_gamepad_training_replay.msg import ButtonValues

class Buttons(object):
    def __init__(self):
        self._joy_sub = rospy.Subscriber('/joy', Joy, self.joy_callback, queue_size=1)
        self._btm_pub = rospy.Publisher('/buttons', ButtonValues, queue_size=1)

    def joy_callback(self, joy_msg):
        b = ButtonValues()
        if joy_msg.buttons[5] == 1 and joy_msg.buttons[4] == 0:
            b.training = True
        else:
            b.training = False

        if joy_msg.buttons[4] == 1 and joy_msg.buttons[5] == 0:
            b.replay = True
        else:
            b.replay = False

        self._btm_pub.publish(b)
        

if __name__ == '__main__':
    rospy.init_node('button_control', anonymous=True)
    button_control = Buttons()
    try:
        rospy.spin()
    except KeyboardInterrapt:
        print("Shutting down")
