import socket
from grSimPy.grSimMessages import ActionMessageSerializer, VisionMessageSerializer
import struct


import grSimPy.proto.proto_py.messages_robocup_ssl_geometry_pb2 as Geometry
import grSimPy.proto.proto_py.messages_robocup_ssl_detection_pb2 as Detection
import grSimPy.proto.proto_py.messages_robocup_ssl_robot_status_pb2 as Status
import grSimPy.proto.proto_py.messages_robocup_ssl_wrapper_pb2 as Wrapper


class grSimVision:
    def __init__(self, vision_host="224.5.23.2", vision_port=10020):
        self.vision_host = vision_host
        self.vision_port = vision_port

        self.vision_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.vision_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.vision_socket.bind((self.vision_host, self.vision_port))
        self.vision_socket.setsockopt(socket.IPPROTO_IP,
                            socket.IP_ADD_MEMBERSHIP,
                            struct.pack("=4sl",
                                        socket.inet_aton(self.vision_host),
                                        socket.INADDR_ANY))

        self.vision = VisionMessageSerializer()
        
    def receive(self):
        recv = self.vision_socket.recv(65536) #65536 #10240
        self.vision.parse_msg(recv)
        self.vision.get_detection_pkt()
        # self.vision.get_geometry_pkt()
        return recv

    def get_robots(self, detection_pkt=None):
        return self.vision.get_robots(detection_pkt=detection_pkt)
    
    def get_robot(self, robot_id, detection_pkt=None, team="blue"):
        return self.vision.get_robot(robot_id=robot_id, detection_pkt=detection_pkt, team=team)
    
    def get_position(self, robot=None, robot_id=None, team="blue"):
        return self.vision.get_position(robot=robot, robot_id=robot_id, team=team)
    
    def get_orientation(self, robot=None, robot_id=None, team="blue"):
        return self.vision.get_orientation(robot=robot, robot_id=robot_id, team=team)
       
    def get_confidence(self, robot=None, robot_id=None, team="blue"):
        return self.vision.get_confidence(robot=robot, robot_id=robot_id, team=team)

    def __del__(self):
        self.vision_socket.close()

class grSimRobot:
    def __init__(self, robot_id, yellow_team=False,
                 grSim_host="127.0.0.1", grSim_port=20011):
            
        self.grSim_host = grSim_host
        self.grSim_port = grSim_port
    
        self.grSim_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.grSim_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        self.action = ActionMessageSerializer(robot_id, yellow_team)    


    def send(self):
        msg = self.action.parse_msg()
        self.grSim_socket.sendto(msg, (self.grSim_host, self.grSim_port))

    def __del__(self):
        self.grSim_socket.close()

if __name__ == "__main__":
    from time import sleep

    robot = grSimRobot(robot_id=1, yellow_team=False)
    vision = grSimVision()
    while(True):
        vision.receive()
        vision.get_robots()
        robot.action.set_velocity(1,1,1)
        robot.send()

        print(vision.get_position(robot_id=1))

    robot.action.set_velocity(0,0,0)
    robot.send()
    for i in range(10):
        robot.action.set_velocity((i%2)*(-2)+1,0,0)
        robot.send()
        sleep(1)
    robot.action.set_velocity(0,0,0)
    robot.send()