#!/usr/bin/env python

import subprocess
import rospy
import time
from nav_msgs.msg import Odometry
from tf.transformations import euler_from_quaternion
from geometry_msgs.msg import Point, Twist
from math import atan2

x = 0.0
y = 0.0 
theta = 0.0

def newOdom(msg):
    global x
    global y
    global theta

    x = msg.pose.pose.position.x
    y = msg.pose.pose.position.y

    rot_q = msg.pose.pose.orientation
    (roll, pitch, theta) = euler_from_quaternion([rot_q.x, rot_q.y, rot_q.z, rot_q.w])

rospy.init_node("speed_controller")

sub = rospy.Subscriber("/odometry/filtered", Odometry, newOdom)
pub = rospy.Publisher("/cmd_vel", Twist, queue_size = 1)

speed = Twist()

r = rospy.Rate(4)

goal = Point()
goal.x = 5
goal.y = 5

count = 5
i = 1
fileName = "pic" + str(i) + ".jpg"
subprocess.call("fswebcam -d /dev/video0 -r 1024x768 -S0 "+fileName,shell=True) 
time.sleep(3)
print('PIC CAPTURED')

while not rospy.is_shutdown():
    inc_x = goal.x -x
    inc_y = goal.y -y

    angle_to_goal = atan2(inc_y, inc_x)

    if abs(angle_to_goal - theta) > 0.1:
        speed.linear.x = 0.1
        speed.angular.z = -0.5         
    else:
        speed.linear.x = 0.5
        speed.angular.z = 0.0

    print('count: ' + str(count))
    print('i: ' + str(i))
    print('count % 2: ' + str(count % 2))
    
    if i == 1 or i == 3 or i == 5::
        fileName = "pic" + str(i) + ".jpg"
        subprocess.call("fswebcam -d /dev/video0 -r 1024x768 -S0 "+fileName,shell=True) 
        time.sleep(3)
        print('PIC CAPTURED')

    i =+ 1
    count =- 1
    time.sleep(3);    
    pub.publish(speed)
    r.sleep()

#rospy.signal_shutdown("done")
