#!/usr/bin/env python3

import rospy
from ros_introduction_pkg.msg import sensor
import random


def talker():
    pub = rospy.Publisher('sensor_data', sensor, queue_size=10)
    rospy.init_node('Sensor_data_publisher', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    for i in range(0,1000):
        msg = sensor()
        msg.Sensor_id= 234
        msg.Sensor_name="Temperature Sensor"
        msg.temperature=33.2 + (random.random()*5)
        
        # rospy.loginfo(msg)
        pub.publish(msg)
        rate.sleep()


if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass