#!/bin/bash

docker build -f pgdocker/Dockerfile -t pgdocker - < pgdocker.tar.gz &&\
docker run --rm -v $PWD/Test:/data pgdocker
