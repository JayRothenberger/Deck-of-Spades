#!/bin/bash

apt-get update
apt-get install -y --fix-missing libgl1-mesa-dev libopenal1 libopenal-dev libglfw3-dev libenet-dev libglew-dev git cmake python3.10 python3-pip libudev1 libudev-dev python3-uinput python3.11-venv xorg supervisor xfce4 xfce4-terminal xterm dbus-x11 libdbus-glib-1-2 tigervnc-standalone-server
cd /vagrant
git clone https://github.com/ebiggers/libdeflate
git clone https://github.com/xtreme8000/BetterSpades

cd /vagrant/libdeflate
cmake -B build && cmake --build build

cd /vagrant/BetterSpades/build
cp /vagrant/libdeflate/build/libdeflate.a /vagrant/BetterSpades/deps/libdeflate.a
cmake /vagrant/BetterSpades/
make

cd /vagrant/printscrn
gcc -shared -O3 -fPIC -Wl,-soname,prtscn -o prtscn.so prtscn.c  -lX11

startx &
export DISPLAY=:1.0

python3 -m venv /home/venv
source /home/venv/bin/activate
pip3 install asyncvnc Pillow

cd /vagrant/python-uinput-master
python3 setup.py build
python3 setup.py install

modprobe -i uinput
# RUN modprobe uinput

cd /vagrant/BetterSpades/build/BetterSpades
./client -aos://3770404938:32887 &

# python3 /vagrant/uinput_server.py &

python3 /vagrant/vncpython/run.py
# startxfce4

