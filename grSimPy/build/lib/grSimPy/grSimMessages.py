import grSimPy.proto.proto_py.grSim_Packet_pb2 as Packet
import grSimPy.proto.proto_py.messages_robocup_ssl_geometry_pb2 as Geometry
import grSimPy.proto.proto_py.messages_robocup_ssl_detection_pb2 as Detection
import grSimPy.proto.proto_py.messages_robocup_ssl_robot_status_pb2 as Status
import grSimPy.proto.proto_py.messages_robocup_ssl_wrapper_pb2 as Wrapper

class VisionMessageSerializer():
    def __init__(self):
        self.wrapper_pkt = Wrapper.SSL_WrapperPacket()
        self.detection_pkt = None
        self.geometry_pkt = None
        self.robots = {"yellow": None, "blue": None}
        # self.detection_pkt = Detection.SSL_DetectionFrame()
        # self.geometry_pkt = Geometry.SSL_GeometryPacket()
    
    def parse_msg(self, msg):
        self.wrapper_pkt.ParseFromString(msg)
    
    def get_wrapper_pkt(self):
        return self.wrapper_pkt
    
    def get_detection_pkt(self, wrapper_pkt=None):
        if(wrapper_pkt is None):
            wrapper_pkt = self.wrapper_pkt
           
        detection_pkt = wrapper_pkt.detection 
        if(detection_pkt.ByteSize() > 0):
            self.detection_pkt = detection_pkt
            return self.detection_pkt
        return None
        
    def get_robots(self, detection_pkt=None):
        if(detection_pkt is None):
            detection_pkt = self.detection_pkt
            
        robots_blue = detection_pkt.robots_blue
        robots_yellow = detection_pkt.robots_yellow
        if(len(robots_blue) > 0):
            self.robots["blue"] = robots_blue

        if(len(robots_yellow) > 0):
            self.robots["yellow"] = robots_yellow
            
        return self.robots

    # robots_yellow {
    #     confidence: 1.0
    #     robot_id: 4
    #     x: 2497.6259765625
    #     y: -1.457729201020594e-13
    #     orientation: 3.1415927410125732
    #     pixel_x: 2497.6259765625
    #     pixel_y: -1.457729201020594e-13
    # }
    def get_robot(self, robot_id, detection_pkt=None, team="blue"):
        self.get_robots(detection_pkt)
        robots = self.robots[team.lower()]
        if(robots is not None):
            for robot in robots:
                if(robot.robot_id == robot_id):
                    return robot
        return None
    
    def get_position(self, robot=None, robot_id=None, team="blue"):
        if(robot is None):
            robot = self.get_robot(robot_id=robot_id, team=team)
            if(robot is None):
                return None    
        return (robot.x, robot.y)
    
    def get_orientation(self, robot=None, robot_id=None, team="blue"):
        if(robot is None):
            robot = self.get_robot(robot_id=robot_id, team=team)
            if(robot is None):
                return None    
        return robot.orientation
       
    def get_confidence(self, robot=None, robot_id=None, team="blue"):
        if(robot is None):
            robot = self.get_robot(robot_id=robot_id, team=team)
            if(robot is None):
                return None    
        return robot.confidence
        
     
    # geometry {
    #     field {
    #         field_length: 12000
    #         field_width: 9000
    #         goal_width: 1200
    #         goal_depth: 200
    #         boundary_width: 300
    #         field_lines {
    #         name: "TopTouchLine"
    #         p1 {
    #             x: -5995.0
    #             y: 4495.0
    #         }
    #         p2 {
    #             x: 5995.0
    #             y: 4495.0
    #         }
    #         thickness: 10.0
    #         }
    #         field_lines {
    #         name: "BottomTouchLine"
    #         p1 {
    #             x: -5995.0
    #             y: -4495.0
    #         }
    #         p2 {
    #             x: 5995.0
    #             y: -4495.0
    #         }
    #         thickness: 10.0
    #         }
    #         field_lines {
    #         name: "LeftGoalLine"
    #         p1 {
    #             x: -5990.0
    #             y: -4495.0
    #         }
    #         p2 {
    #             x: -5990.0
    #             y: 4495.0
    #         }
    #         thickness: 10.0
    #         }
    #         field_lines {
    #         name: "RightGoalLine"
    #         p1 {
    #             x: 5990.0
    #             y: -4495.0
    #         }
    #         p2 {
    #             x: 5990.0
    #             y: 4495.0
    #         }
    #         thickness: 10.0
    #         }
    #         field_lines {
    #         name: "HalfwayLine"
    #         p1 {
    #             x: 0.0
    #             y: -4495.0
    #         }
    #         p2 {
    #             x: 0.0
    #             y: 4495.0
    #         }
    #         thickness: 10.0
    #         }
    #         field_lines {
    #         name: "CenterLine"
    #         p1 {
    #             x: -5990.0
    #             y: 0.0
    #         }
    #         p2 {
    #             x: 5990.0
    #             y: 0.0
    #         }
    #         thickness: 10.0
    #         }
    #         field_lines {
    #         name: "LeftPenaltyStretch"
    #         p1 {
    #             x: -4795.0
    #             y: -1200.0
    #         }
    #         p2 {
    #             x: -4795.0
    #             y: 1200.0
    #         }
    #         thickness: 10.0
    #         }
    #         field_lines {
    #         name: "RightPenaltyStretch"
    #         p1 {
    #             x: 4795.0
    #             y: -1200.0
    #         }
    #         p2 {
    #             x: 4795.0
    #             y: 1200.0
    #         }
    #         thickness: 10.0
    #         }
    #         field_lines {
    #         name: "RightGoalTopLine"
    #         p1 {
    #             x: 5990.0
    #             y: 600.0
    #         }
    #         p2 {
    #             x: 6190.0
    #             y: 600.0
    #         }
    #         thickness: 10.0
    #         }
    #         field_lines {
    #         name: "RightGoalBottomLine"
    #         p1 {
    #             x: 5990.0
    #             y: -600.0
    #         }
    #         p2 {
    #             x: 6190.0
    #             y: -600.0
    #         }
    #         thickness: 10.0
    #         }
    #         field_lines {
    #         name: "RightGoalDepthLine"
    #         p1 {
    #             x: 6185.0
    #             y: -600.0
    #         }
    #         p2 {
    #             x: 6185.0
    #             y: 600.0
    #         }
    #         thickness: 10.0
    #         }
    #         field_lines {
    #         name: "LeftGoalTopLine"
    #         p1 {
    #             x: -5990.0
    #             y: 600.0
    #         }
    #         p2 {
    #             x: -6190.0
    #             y: 600.0
    #         }
    #         thickness: 10.0
    #         }
    #         field_lines {
    #         name: "LeftGoalBottomLine"
    #         p1 {
    #             x: -5990.0
    #             y: -600.0
    #         }
    #         p2 {
    #             x: -6190.0
    #             y: -600.0
    #         }
    #         thickness: 10.0
    #         }
    #         field_lines {
    #         name: "LeftGoalDepthLine"
    #         p1 {
    #             x: -6185.0
    #             y: -600.0
    #         }
    #         p2 {
    #             x: -6185.0
    #             y: 600.0
    #         }
    #         thickness: 10.0
    #         }
    #         field_lines {
    #         name: "LeftFieldLeftPenaltyStretch"
    #         p1 {
    #             x: -5990.0
    #             y: 1200.0
    #         }
    #         p2 {
    #             x: -4790.0
    #             y: 1200.0
    #         }
    #         thickness: 10.0
    #         }
    #         field_lines {
    #         name: "LeftFieldRightPenaltyStretch"
    #         p1 {
    #             x: -5990.0
    #             y: -1200.0
    #         }
    #         p2 {
    #             x: -4790.0
    #             y: -1200.0
    #         }
    #         thickness: 10.0
    #         }
    #         field_lines {
    #         name: "RightFieldLeftPenaltyStretch"
    #         p1 {
    #             x: 5990.0
    #             y: -1200.0
    #         }
    #         p2 {
    #             x: 4790.0
    #             y: -1200.0
    #         }
    #         thickness: 10.0
    #         }
    #         field_lines {
    #         name: "RightFieldRightPenaltyStretch"
    #         p1 {
    #             x: 5990.0
    #             y: 1200.0
    #         }
    #         p2 {
    #             x: 4790.0
    #             y: 1200.0
    #         }
    #         thickness: 10.0
    #         }
    #         field_arcs {
    #         name: "CenterCircle"
    #         center {
    #             x: 0.0
    #             y: 0.0
    #         }
    #         radius: 495.0
    #         a1: 0.0
    #         a2: 6.2831854820251465
    #         thickness: 10.0
    #         }
    #     }
    #     }
    def get_geometry_pkt(self):
        pass
class ActionMessageSerializer:
    def __init__(self, robot_id, team):
        self.original_msg = {
                                "id"            : robot_id,
                                "kickspeedx"    : 0,
                                "kickspeedz"    : 0,
                                "veltangent"    : 0,
                                "velnormal"     : 0,
                                "velangular"    : 0,
                                "spinner"       : False,
                                "wheelsspeed"   : False,
                                "timestamp"     : 0,
                                "isteamyellow"  : team,
                                "wheel1"        : 0.0,
                                "wheel2"        : 0.0,
                                "wheel3"        : 0.0,
                                "wheel4"        : 0.0,
                            }
        self.action = self.original_msg.copy()
    
    def get_msg_template(self):
        return self.original_msg

    def get_action(self):
        return self.action

    def set_velocity_x(self, vel):
        self.action["veltangent"] = vel

    def set_velocity_y(self, vel):
        self.action["velnormal"] = vel
    
    def set_velocity_w(self, vel):
        self.action["velangular"] = vel

    def set_velocity(self, x_vel, y_vel, w_vel):
        self.set_velocity_x(x_vel)
        self.set_velocity_y(y_vel)
        self.set_velocity_w(w_vel)
        
    def set_actions(self, actions_dict):
        self.action = dict(self.original_msg, **actions_dict)
    
    def parse_msg(self, msg=None):
        """
        Function creates a message to grSim using protobuf
        rasing error if some error occured related to the input message
        params in the dictionary with these fields:
            "id" - (int) robot's id
            "isteamyellow" - (bool) true if robot is yellow
            "kickspeedx" - (float)
            "kickspeedz" - (float)
            "veltangent" - (float)
            "velnormal" - (float)
            "velangular" - (float)
            "spinner" - (bool)
            "wheelsspeed" - (bool) true if you want to control each wheel directly
            "timestamp" - (float) idk why we need it just pass 0.0
            "wheel1" - (float)
            "wheel2" - (float)
            "wheel3" - (float)
            "wheel4" - (float)
        Return:
            String: serialized message with all the actions for the robot to be sent
        """
        data = None
        if(msg is not None):
            if(set(msg.keys()) != set(self.original_msg.keys())):
                raise KeyError("Attempt to send a message without all the required data or have extra data")
            data = dict(self.original_msg, **msg)
        
        else:
            data = self.action
            
        message = Packet.grSim_Packet()
        commands = message.commands.robot_commands.add()
        commands.id                     = data["id"]
        message.commands.isteamyellow   = data["isteamyellow"]
        commands.kickspeedx             = data["kickspeedx"]
        commands.kickspeedz             = data["kickspeedz"]
        commands.veltangent             = data["veltangent"]
        commands.velnormal              = data["velnormal"]
        commands.velangular             = data["velangular"]
        commands.spinner                = data["spinner"]
        commands.wheelsspeed            = data["wheelsspeed"]
        message.commands.timestamp      = data["timestamp"]
        commands.wheel1                 = data["wheel1"]
        commands.wheel2                 = data["wheel2"]
        commands.wheel3                 = data["wheel3"]
        commands.wheel4                 = data["wheel4"]
            
        return message.SerializeToString()
