#!/bin/sh
rm -rf ../proto_py
mkdir ../proto_py
echo "proto_py" > ../.gitignore
touch ../__init__.py
touch ../proto_py/__init__.py
protoc --python_out=../proto_py *.proto


sed -i '16s/.*/import grSimPy.proto.proto_py.grSim_Commands_pb2 as grSim__Commands__pb2/' ../proto_py/grSim_Packet_pb2.py
sed -i '17s/.*/import grSimPy.proto.proto_py.grSim_Replacement_pb2 as grSim__Replacement__pb2/' ../proto_py/grSim_Packet_pb2.py

sed -i '16s/.*/import grSimPy.proto.proto_py.messages_robocup_ssl_detection_pb2 as messages__robocup__ssl__detection__pb2/' ../proto_py/messages_robocup_ssl_wrapper_pb2.py
sed -i '17s/.*/import grSimPy.proto.proto_py.messages_robocup_ssl_geometry_pb2 as messages__robocup__ssl__geometry__pb2/' ../proto_py/messages_robocup_ssl_wrapper_pb2.py

sed -i '16s/.*/import grSimPy.proto.proto_py.messages_robocup_ssl_detection_pb2 as messages__robocup__ssl__detection__pb2/' ../proto_py/messages_robocup_ssl_refbox_log_pb2.py

