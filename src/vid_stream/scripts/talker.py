#!/usr/bin/env python
# license removed for brevity
import rospy

import numpy as np
import cv2

from cv_bridge import CvBridge
from sensor_msgs.msg import Image

def talker():
    
    cap = cv2.VideoCapture(0)
    cvb = CvBridge()
    
    pub = rospy.Publisher('chatter', Image, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(5) #Hz

    while not rospy.is_shutdown():

	# Capture frame-by-frame
        ret, frame = cap.read()
        if ret:
            frame_copy = frame.copy()
            # convert to ros message
            ros_img = cvb.cv2_to_imgmsg(frame_copy, encoding="bgr8")
            # publish it
            pub.publish(ros_img)
        rate.sleep()
    
    # When everything done, release the capture
    cap.release()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
