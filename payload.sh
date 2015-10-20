#!/bin/sh

ls
pwd
whoami
which apt
which apt-get

echo $SRC_ID_KEY_DATA

apt-get install -y openssh-server

