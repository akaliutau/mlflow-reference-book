#!/bin/bash
docker build -t jpnotebook .
export JUPYTER_TOKEN='123'
docker run -p 8888:8888 -p 5000:5000 -u "$(id -u ${USER})":"$(id -g ${USER})" \
  -e JUPYTER_TOKEN=$JUPYTER_TOKEN \
  -v "$HOME/notebooks/":/home/jovyan/ -it jpnotebook

