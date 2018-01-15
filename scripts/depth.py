#!/usr/bin/env python
# Copyright 2017 TomotakaSuzuki
# Released under the BSD License

import rospy
import cv2
from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
from turtlebot_gamepad_training_replay.msg import DepthSensorValues

class Depth_estimater(object):
    def __init__(self):
        self._bridge = CvBridge()
        self._dep_pub = rospy.Publisher('/DepthSensor', DepthSensorValues, queue_size=1)
        self._depimg_sub = rospy.Subscriber('/camera/depth/image', Image, self.depth_image_callback, queue_size=1)

    def depth_image_callback(self, depth_data):
        try:
            depth_image = self._bridge.imgmsg_to_cv2(depth_data, "passthrough")
        except CvBridgeError as e:
            print(e)

        (rows, cols) = depth_image.shape
        
        d = DepthSensorValues()
        d.right_side = depth_image[120][560]
        d.right_center = depth_image[120][400]
        d.left_center = depth_image[120][240]
        d.left_side = depth_image[120][80]
        d.sum_center = d.left_center + d.right_center
        d.sum_all = d.sum_center + d.left_side + d.right_side

        try:
            self._dep_pub.publish(d)
        except CvBridgeError as e:
            print(e)

if __name__ == '__main__':
    rospy.init_node('get_depth', anonymous=True)
    depth_scan = Depth_estimater()
    try:
        rospy.spin()
    except KeyboardInterrapt:
        print("Shutting down")
        cv2.destroyAllWindow()

