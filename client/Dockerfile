## Custom Dockerfile
FROM consol/debian-xfce-vnc
ENV REFRESHED_AT 2023-11-10

# Switch to root user to install additional software
USER 0

## Install a gedit
RUN apt-get update
RUN apt-get install -y --fix-missing libgl1-mesa-dev libopenal1 libopenal-dev libglfw3-dev libenet-dev libglew-dev git cmake
# need to copy the code from local with libdeflate
WORKDIR /src
RUN git clone https://github.com/ebiggers/libdeflate
WORKDIR /src/libdeflate
RUN cmake -B build && cmake --build build
WORKDIR /src
RUN git clone https://github.com/xtreme8000/BetterSpades
WORKDIR /src/BetterSpades/build
RUN cp /src/libdeflate/build/libdeflate.a /src/BetterSpades/deps/libdeflate.a
RUN cmake ..
RUN make
WORKDIR /src/BetterSpades/build/BetterSpades
CMD ./client
## switch back to default user
USER 1000