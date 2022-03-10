#!/bin/bash

# All need to be done at super user level
# sudo sh run_marking.sh 
if [[ "$OSTYPE" != "darwin"* ]]; then
    systemctl start docker
else
    echo "macos - skipping systemctl!"
fi

docker build -t a1docker - < FSADA1Docker
docker run --rm -v "$PWD/Test:/marking" a1docker

systemctl stop docker
