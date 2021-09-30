#!/usr/bin/env python
import rospy
import random
from bol_2_prog2.msg import msg_ex

rospy.init_node('node2')


pub=rospy.Publisher('resultado',msg_ex,queue_size=1)

rate=rospy.Rate(1)

mis_datos=msg_ex()

def callback(msg):
    if msg.resultado==False:
        mis_datos.resultado=[False,True][random.randint(0,1)]
        pub.publish(mis_datos)
        print('Enviado...')
    else:
        print('Acabar bucle')


sub=rospy.Subscriber('objetivo_presa',msg_ex,callback)