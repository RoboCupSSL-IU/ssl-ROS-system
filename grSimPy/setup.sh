#!/bin/sh
current_dir=$PWD
proto_dir=$current_dir"/src/grSimPy/proto/src/"
cd $proto_dir && sh compile.sh
cd $current_dir
sudo python3 setup.py install