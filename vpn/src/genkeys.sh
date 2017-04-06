#!/bin/bash

cd /usr/share/easy-rsa
source ./vars
./clean-all
./pkitool --initca
./build-key-server --batch server
./build-key client
./build-dh
