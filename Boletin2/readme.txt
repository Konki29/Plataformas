#!/usr/bin/env python
import rospy
import random
from turtlesim.srv import Spawn, SpawnRequest, Kill,KillRequest
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose

rospy.init_node('nodo')

rospy.wait_for_service('/spawn')
servicio = rospy.ServiceProxy('/spawn',Spawn)
peticion=SpawnRequest()
peticion.name='presa'
peticion.x=5
peticion.y=10
peticion.theta=3.1416
servicio(peticion)

peticion.name='depredador'
peticion.x=5
peticion.y=5
peticion.theta=6
servicio(peticion)

rospy.wait_for_service('/kill')
servicio = rospy.ServiceProxy('/kill',Kill)
borrar=KillRequest()
borrar.name='turtle1'
servicio(borrar)


xb=presa.x-depredador.x     
yb=presa.y-depredador.y 
distancia=math.sqrt(math.pow(xb,2)+math.pow(yb,2))

while distancia>2 and not rospy.is_shutdown(): 
    vel_linear_x = 1.5 * math.sqrt(math.pow((presa_x - depredador_x), 2) + math.pow((presa_y - depredador_y), 2))
    vel_angular_z = 4 * (math.atan2(presa_y - depredador_y, presa_x - depredador_x) - depredador_theta)
    xb=presa.x-depredador.x     
    yb=presa.y-depredador.y     
    distancia=math.sqrt(math.pow(xb,2)+math.pow(yb,2))          
    velpresa.linear.x=0.3     
    velpresa.angular.z=0.08          
    veldepredador.linear.x=vel_linear_x*0.119     
    veldepredador.angular.z=vel_angular_z
