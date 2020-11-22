#!/bin/sh
proto_dir=$PWD"/src/grSimPy/proto"
# echo $proto_dir"/src/"

rm -rf $proto_dir"/proto_py"
mkdir $proto_dir"/proto_py"
echo "proto_py" > $proto_dir"/.gitignore"
touch $proto_dir"/__init__.py"
touch $proto_dir"/proto_py/__init__.py"
protoc --python_out=$proto_dir"/proto_py" --proto_path=$proto_dir"/src/" $(find $proto_dir -iname "*.proto") 

sed -i '16s/.*/import grSimPy.proto.proto_py.grSim_Commands_pb2 as grSim__Commands__pb2/' $proto_dir/proto_py/grSim_Packet_pb2.py
sed -i '17s/.*/import grSimPy.proto.proto_py.grSim_Replacement_pb2 as grSim__Replacement__pb2/' $proto_dir/proto_py/grSim_Packet_pb2.py

sudo python3 setup.py install