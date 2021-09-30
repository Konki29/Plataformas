#!/usr/bin/env python
import rospy
from publicador.msg import datos

rospy.init_node('publicador_customizado')
pub=rospy.Publisher('mensaje_personalizado',datos,queue_size=1)
rate=rospy.Rate(2)
mis_datos=datos()
mis_datos.edad=20
mis_datos.nombre="carlos maricon"
mis_datos.coeficiente=3.5
while not rospy.is_shutdown():
    pub.publish(mis_datos)
    rate.sleep()