#!/usr/bin/env python
import rospy
import random
from bol_2_prog1.msg import msg_ex

rospy.init_node('nodo')


pub=rospy.Publisher('objetivo_presa',msg_ex,queue_size=1)
rate=rospy.Rate(1)

mis_datos=msg_ex()

mis_datos.x=1
mis_datos.y=3
while not rospy.is_shutdown():
    pub.publish(mis_datos)
rate.sleep()

def callback(msg):
    if msg.resultado==True:
        print("test")
    else:
        mis_datos.x=random.randint(0,10)
        mis_datos.y=random.randint(0,10)
        pub.publish(mis_datos)


sub=rospy.Subscriber('resultado',msg_ex,callback)
rospy.spin()