#!/usr/bin/env python3

import rospy
from ros_introduction_pkg.msg import sensor

def callback(msg):
    rospy.loginfo('Received Data: id-> %d, name-> %s, temparature-> %0.2f', msg.Sensor_id, msg.Sensor_name, msg.temperature)


def listener():

    rospy.init_node('sensor_data_subscriber', anonymous=True)

    rospy.Subscriber('sensor_data', sensor, callback)

    rospy.spin()

if __name__ == '__main__':
    listener()