#!/usr/bin/env python
import rospy 
from gestor_segunda_oportunidad.msg import datos

dato=datos()


rospy.init_node("sub")

sub=rospy.Subscriber("consigna",datos,callback)
def callback(msg):
    print("Accion a tomar : ",msg.comando)
    print("Valor tiempo random",msg.tiempo)
    print()
    print("Valor de la posicion")
    print(msg.posi.position.x)
    print(msg.posi.position.y)
    print(msg.posi.position.z)
    print()
    print(msg.posi.orientation.x)
    print(msg.posi.orientation.y)
    print(msg.posi.orientation.z)
rospy.spin()