import grSimPy.proto.proto_py.grSim_Packet_pb2 as Packet

class ActionMessageSerializer:
    def __init__(self):
        self.original_msg = {
                                "id"            : 0,
                                "kickspeedx"    : 0,
                                "kickspeedz"    : 0,
                                "veltangent"    : 0,
                                "velnormal"     : 0,
                                "velangular"    : 0,
                                "spinner"       : False,
                                "wheelsspeed"   : False,
                                "timestamp"     : 0,
                                "isteamyellow"  : False,
                                "wheel1"        : 0.0,
                                "wheel2"        : 0.0,
                                "wheel3"        : 0.0,
                                "wheel4"        : 0.0,
                            }
    
    def get_msg_template(self):
        return self.original_msg

    def get_serialized_msg(self, msg: dict) -> bytes:
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
        """
        if(set(msg.keys()) != set(self.original_msg.keys())):
            raise KeyError("Attempt to send a message without all the required data or have extra data")
        
        data = dict(self.original_msg, **msg)

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
        # print(message)

        return message.SerializeToString()
