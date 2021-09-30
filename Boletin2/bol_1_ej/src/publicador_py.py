#!/usr/bin/env python
import rospy
import random
from bol_1_ej.msg import datos

rospy.init_node('publicador_customizado')
pub=rospy.Publisher('consigna',datos,queue_size=1)
rate=rospy.Rate(1)
mis_datos=datos()
while not rospy.is_shutdown():
    mis_datos.comando=["inicio","continuar","interrumpir"][random.randint(0,2)]
    mis_datos.tiempo=random.randint(30,100) 
    mis_datos.posi.position.x=random.randint(-100,100)
    mis_datos.posi.position.y=random.randint(-100,100)
    mis_datos.posi.position.z=random.randint(-100,100)

    mis_datos.posi.orientation.x=random.randint(-100,100)
    mis_datos.posi.orientation.y=random.randint(-100,100)
    mis_datos.posi.orientation.z=random.randint(-100,100)
    pub.publish(mis_datos)
    rate.sleep()