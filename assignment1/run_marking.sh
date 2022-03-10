#!/bin/bash

# All need to be done at super user level
# sudo sh run_marking.sh 
systemctl start docker

docker build -t a1docker - < FSADA1Docker
docker run --rm -v "$PWD/Test:/marking" a1docker

systemctl stop docker
