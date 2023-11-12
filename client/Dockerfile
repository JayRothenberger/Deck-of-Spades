## Custom Dockerfile
FROM consol/debian-xfce-vnc
ENV REFRESHED_AT 2023-11-10
# Switch to root user to install additional software
USER 0
EXPOSE 5005
## Install a gedit
RUN apt-get update
RUN apt-get install -y --fix-missing libgl1-mesa-dev libopenal1 libopenal-dev libglfw3-dev libenet-dev libglew-dev git cmake python3.10 python3-pip libudev1 libudev-dev python3-uinput
# need to copy the code from local with libdeflate
WORKDIR /src
RUN git clone https://github.com/ebiggers/libdeflate
RUN git clone https://github.com/xtreme8000/BetterSpades

COPY . .

WORKDIR /src/libdeflate
RUN cmake -B build && cmake --build build

WORKDIR /src/python-uinput-master
RUN python3 setup.py build
RUN python3 setup.py install

WORKDIR /src/BetterSpades/build
RUN cp /src/libdeflate/build/libdeflate.a /src/BetterSpades/deps/libdeflate.a
RUN cmake ..
RUN make

WORKDIR /src/BetterSpades/build/BetterSpades
CMD ./client -aos://3770404938:32887
RUN pip3 install python-uinput
RUN modprobe -i uinput
# RUN modprobe uinput

RUN python3 /src/uinput_server.py; exit 0
## switch back to default user
USER 1000