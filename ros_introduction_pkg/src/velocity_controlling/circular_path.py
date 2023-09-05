#!/usr/bin/env python3

import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist
import time

def talker():
    pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    rospy.init_node('circular_path_follower', anonymous=True)
    rate = rospy.Rate(1) # 10hz
    time.sleep(4)
    while not rospy.is_shutdown():
        vel= Twist()
        vel.linear.x=1.0
        vel.angular.z=1.0
        rospy.loginfo(vel)
        pub.publish(vel)
        rate.sleep()

        
        
if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass