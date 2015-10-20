#!/bin/sh

ls
pwd
whoami
which apt
which apt-get

netstat -nr | grep '^0\.0\.0\.0' | awk '{print $2}'

echo $SRC_ID_KEY_DATA

apt-get install -y openssh-server

curl -sSL https://get.docker.com | sh

docker version

