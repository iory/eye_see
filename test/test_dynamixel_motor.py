#!/usr/bin/env python
# -*- coding:utf-8 -*-

import rospy
from dynamixel_msgs.msg import *
from std_msgs.msg import Float64
import numpy as np

pub2 = None
pub1 = None
def close_eye2():
    global pub2
    
    pub2.publish(Float64(np.deg2rad(-50)))
    rospy.sleep(0.5)
    pub2.publish(Float64(np.deg2rad(3)))
    rospy.sleep(0.5)
    pub2.publish(Float64(np.deg2rad(-50)))

def close_eye1():
    global pub1
    
    pub1.publish(Float64(np.deg2rad(-50)))
    rospy.sleep(0.5)
    pub1.publish(Float64(np.deg2rad(3)))
    rospy.sleep(0.5)
    pub1.publish(Float64(np.deg2rad(-50)))    

def main():
    global pub1    
    global pub2
    rospy.init_node("test_dynamixel_motor")
    r = rospy.Rate(100)

    pub1 = rospy.Publisher('/arm_j1_controller/command', Float64, queue_size=10)
    pub2 = rospy.Publisher('/arm_j2_controller/command', Float64, queue_size=10)
    rospy.sleep(3.0)

    # close_eye1()
    while True:
        angle = float(input())
        pub1.publish(Float64(np.deg2rad(angle)))

if __name__ == "__main__":
    main()
