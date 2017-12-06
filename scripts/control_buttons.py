import rospy
from sensor_msgs.msg import Joy
from turtlebot_gamepad_training_replay import ButtonValues

class Buttons(object):
    def __init__(self):
        self._joy_sub = Subscriber('/joy', Joy, self.joy_callback, queue_size=1)
        self._btm_pub = Publisher('/buttons', ButtonValues, queue_size=1)

    def joy_callback(self, joy_msg):
        b = ButtonValues()
        if joy_msg.buttons[7] == 1:
            b.training = True
        else
            b.training = False

        if joy_msg.buttons[6] == 1:
            b.replay = True
        else
            b.replay = False

        self._btm_pub.publish(b)
        

if __name__ == '__main__':
    rospy.init_node('button_control', anonymous=True)
    button_control = Buttons()
    try:
        rospy.spin()
    except KeyboardInterrapt:
        print("Shutting down")
