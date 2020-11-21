import socket
import sys
# import proto_py
import proto_py.grSim_Packet_pb2 as Packet

class grSimMessage:
    def __init__(self, params: dict) -> bool:
        """
        Function creates message to grSim using protobuf
        returns False if some error occured
        params is dictionary with these fields:
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
        required_keys = [
            "id",
            "isteamyellow",
            "kickspeedx",
            "kickspeedz",
            "veltangent",
            "velnormal",
            "velangular",
            "spinner",
            "wheelsspeed",
            "timestamp",
            "wheel1",
            "wheel2",
            "wheel3",
            "wheel4"
        ]

        self.data = params

        for key in required_keys:
            try:
                params[key]
            except:
                print(key)
                self.data = False
                break

    def getSerializedMessage(self) -> bytes:
        if not self.data:
            raise ZeroDivisionError("Attempt to send package without all data")
        message = Packet.grSim_Packet()
        commands = message.commands.robot_commands.add()
        commands.id                 = self.data["id"]
        message.commands.isteamyellow       = self.data["isteamyellow"]
        commands.kickspeedx         = self.data["kickspeedx"]
        commands.kickspeedz         = self.data["kickspeedz"]
        commands.veltangent         = self.data["veltangent"]
        commands.velnormal          = self.data["velnormal"]
        commands.velangular         = self.data["velangular"]
        commands.spinner            = self.data["spinner"]
        commands.wheelsspeed         = self.data["wheelsspeed"]
        message.commands.timestamp          = self.data["timestamp"]
        commands.wheel1             = self.data["wheel1"]
        commands.wheel2             = self.data["wheel2"]
        commands.wheel3             = self.data["wheel3"]
        commands.wheel4             = self.data["wheel4"]

        return message.SerializeToString()



HOST, PORT = "127.0.0.1", 20011

message = grSimMessage({
    "id"            : 0,
    "kickspeedx"    : 0,
    "kickspeedz"    : 0,
    "veltangent"    : 0,
    "velnormal"     : 0,
    "velangular"    : 0,
    "spinner"       : False,
    "wheelsspeed"    : False,
    "timestamp"     : 0,
    "isteamyellow"  : False,
    "wheel1"        : 0.0,
    "wheel2"        : 0.0,
    "wheel3"        : 0.0,
    "wheel4"        : 0.0,
})

a = message.getSerializedMessage()

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
    while True:
        sock.sendto(a, (HOST, PORT))
        exit()
