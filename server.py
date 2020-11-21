import proto_py.grSim_Packet_pb2 as Packet
import socket

UDP_IP = "127.0.0.1"
UDP_PORT = 20011

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

message = Packet.grSim_Packet()

while True:
    data, addr = sock.recvfrom(1024)
    message.ParseFromString(data)
    print(message)