import socket
import uinput

if __name__ == "__main__":
    UDP_IP = "127.0.0.1"
    UDP_PORT = 5005

    sock = socket.socket(socket.AF_INET, # Internet
                        socket.SOCK_DGRAM) # UDP
    sock.bind((UDP_IP, UDP_PORT))

    cmd_strings = []

    with open('/src/python-uinput-master/src/ev.py', 'r') as fp:
        for line in fp.readlines():
            cmd_strings.append(line.split(' ')[0])

    # tuple([getattr(uinput, cmd) for cmd in cmd_strings])
    events = (uinput.REL_X, uinput.REL_Y)

    with uinput.Device(events) as device:

        while True:
            emit = True

            data, addr = sock.recvfrom(256).decode('utf8') # buffer size is 256 bytes
            print(data)
            cmd, fn, value, syn = data.split(':')

            if cmd == 'emit':
                emit = True

            fn = getattr(input_device, fn)
            cmd = getattr(uinput, cmd)
            value = int(value)
            syn = bool(syn)

            if emit:
                fn(cmd, value, syn)
            else:
                fn(cmd, syn)