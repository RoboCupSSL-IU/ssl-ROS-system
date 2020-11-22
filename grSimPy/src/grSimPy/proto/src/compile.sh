#!/bin/sh
rm -rf ../proto_py
mkdir ../proto_py
echo "proto_py" > ../.gitignore
touch ../__init__.py
touch ../proto_py/__init__.py
protoc --python_out=../proto_py *.proto
