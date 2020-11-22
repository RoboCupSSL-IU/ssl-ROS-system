import socket
from grSimPy.grSimMessages import ActionMessageSerializer

class grSimRobot:
    def __init__(self, robot_id, yellow_team=False, host="127.0.0.1", port=20011):
        self.host = host
        self.port = port
        self.action_serializer = ActionMessageSerializer()
        self.msg_dict = {
                            "id"            : robot_id,
                            "kickspeedx"    : 0,
                            "kickspeedz"    : 0,
                            "veltangent"    : 0,
                            "velnormal"     : 0,
                            "velangular"    : 0,
                            "spinner"       : False,
                            "wheelsspeed"   : False,
                            "timestamp"     : 0,
                            "isteamyellow"  : yellow_team,
                            "wheel1"        : 0.0,
                            "wheel2"        : 0.0,
                            "wheel3"        : 0.0,
                            "wheel4"        : 0.0,
                        }

    def get_msg_dict(self):
        return self.msg_dict

    def set_msg(self, msg_dict):
        self.msg_dict = dict(self.msg_dict, **msg_dict)
        
    def set_velocity_x(self, vel):
        self.msg_dict["veltangent"] = vel
        self.send()

    def set_velocity_y(self, vel):
        self.msg_dict["velnormal"] = vel
        self.send()
    
    def set_velocity_w(self, vel):
        self.msg_dict["velangular"] = vel
        self.send()

    def set_velocity(self, x_vel, y_vel, w_vel):
        self.set_velocity_x(x_vel)
        self.set_velocity_y(y_vel)
        self.set_velocity_w(w_vel)
        
        
    def send(self):
        msg = self.action_serializer.get_serialized_msg(self.msg_dict)
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
            sock.sendto(msg, (self.host, self.port))