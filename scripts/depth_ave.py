#!/usr/bin/env python
# -*- coding: utf-8 -*-
import rospy
import numpy as np
import cv2
from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
from turtlebot_gamepad_training_replay.msg import DepthSensorValues

class Depth_estimater(object):
    def __init__(self):
        self._bridge = CvBridge()
        self._dep_pub = rospy.Publisher('/DepthSensor', DepthSensorValues, queue_size=1)
        self._depimg_sub = rospy.Subscriber('/camera/depth/image_raw', Image, self.depth_image_callback, queue_size=1)
        
        self.depth_copy = np.zeros((480, 640)) #二次元配列を0で初期化
       
    def depth_image_callback(self, depth_data):
        try:
            depth_image = self._bridge.imgmsg_to_cv2(depth_data, "passthrough")
        except CvBridgeError as e:
            print(e)
        depth_image = np.array(depth_image) #depth_imageをnumpy.array型に変換
        count = 0
        depth_image.flags.writeable = True #depth_imageに書き込みできるようにする
        self.depth_copy.flags.writeable = True 
        #depth_image[np.isnan(depth_image)] = 0 #nanをすべて0に変換
        depth_image = depth_image.reshape(-1,) #一次元配列に変換
        self.depth_copy = self.depth_copy.reshape(-1,) 
        #print(depth_image.shape) #(307200,)
        
        for i in depth_image:
            count += 1
            if (i != i): #iがnanだった場合一つ前の値を代入する
                i = self.depth_copy[count-1]
                depth_image[count-1] = i
        count = 0
        depth_image = depth_image.reshape(480, 640) #二次元配列に戻す
        #print(depth_image)
        d = DepthSensorValues()
        d.right_side = (depth_image[120][556] + depth_image[120][557] + depth_image[120][558] + depth_image[120][559] + depth_image[120][560] + depth_image[120][561] + depth_image[120][562] + depth_image[120][563] + depth_image[120][564] + depth_image[120][565]) / 10 
        d.right_center = (depth_image[120][396] + depth_image[120][397] + depth_image[120][398] + depth_image[120][399] + depth_image[120][400] + depth_image[120][401] + depth_image[120][402] + depth_image[120][403] + depth_image[120][404] + depth_image[120][405]) / 10 
        d.left_center = (depth_image[120][236] + depth_image[120][237] + depth_image[120][238] + depth_image[120][239] + depth_image[120][240] + depth_image[120][241] + depth_image[120][242] + depth_image[120][243] + depth_image[120][244] + depth_image[120][245]) / 10 
        d.left_side = (depth_image[120][76] + depth_image[120][77] + depth_image[120][78] + depth_image[120][79] + depth_image[120][80] + depth_image[120][81] + depth_image[120][82] + depth_image[120][83] + depth_image[120][84] + depth_image[120][85]) / 10
        d.sum_center = d.left_center + d.right_center
        d.sum_all = d.sum_center + d.left_side + d.right_side
        self._dep_pub.publish(d)
   
        self.depth_copy = depth_image

if __name__ == '__main__':
    rospy.init_node('get_depth', anonymous=True)
    depth_scan = Depth_estimater()
    try:
        rospy.spin()
    except KeyboardInterrapt:
        print("Shutting down")
        cv2.destroyAllWindow()

