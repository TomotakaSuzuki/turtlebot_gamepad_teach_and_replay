#!/usr/bin/env python
import rospy
import cv2
import numpy as np
from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError

class Depth_estimater(object):
    def __init__(self):
        self._bridge = CvBridge()
        self._img_pub = rospy.Publisher('/camrera/rgb/image_raw2', Image, queue_size=1)
        self._depimg_pub = rospy.Publisher('/camera/depth/image_raw2', Image, queue_size=1)
        self._img_sub = rospy.Subscriber('/camera/rgb/image_raw', Image, self.image_callback, queue_size=1)
        self._depimg_sub = rospy.Subscriber('/camera/depth/image_raw', Image, self.depth_image_callback, queue_size=1)

    def image_callback(self, image_data):
        try:
            cv_image = self._bridge.imgmsg_to_cv2(image_data, "bgr8")
        except CvBridgeError as e:
            print(e)

        (rows, cols, channels) = cv_image.shape #(y=480, x=640, 3)
        print(cv_image.shape)

        cv_image = cv2.rectangle(cv_image, (370, 190), (270, 290), (0,0,255), 3)
        
        try:
            self._img_pub.publish(self._bridge.cv2_to_imgmsg(cv_image, "bgr8"))
        except CvBridgeError as e:
            print(e)
    
    def depth_image_callback(self, depth_data):
        try:
            # conversion msg->opencv
            depth_image = self._bridge.imgmsg_to_cv2(depth_data, "passthrough")
        except CvBridgeError as e:
            print(e)

        (rows, cols) = depth_image.shape
        for i in depth_image:
            print(i)
        try:
            self._depimg_pub.publish(self._bridge.cv2_to_imgmsg(depth_image, "passthrough"))
        except CvBridgeError as e:
            print(e)

if __name__ == '__main__':
    rospy.init_node('depth_scan', anonymous=True)
    depth_scan = Depth_estimater()
    try:
        rospy.spin()
    except KeyboardInterrapt:
        print("Shutting down")
        cv2.destroyAllWindow()
