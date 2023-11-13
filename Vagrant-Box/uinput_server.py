import socket
import uinput

if __name__ == "__main__":
    print('- running uinput server -')
    UDP_IP = "127.0.0.1"
    UDP_PORT = 5005

    sock = socket.socket(socket.AF_INET, # Internet
                        socket.SOCK_DGRAM) # UDP
    sock.bind((UDP_IP, UDP_PORT))

    cmd_strings = []

    with open('/vagrant/python-uinput-master/src/ev.py', 'r') as fp:
        for line in fp.readlines():
            cmd_strings.append(line.split(' ')[0])

    # events = tuple([getattr(uinput, cmd) for cmd in cmd_strings])
    events = (uinput.KEY_1, uinput.KEY_2, uinput.BTN_LEFT, uinput.REL_X, uinput.REL_Y)

    with uinput.Device(events) as device:

        while True:
            emit = True

            data, addr = sock.recvfrom(256) # buffer size is 256 bytes
            data = data.decode('utf8')
            print(data)
            cmd, fn, value, syn = data.split(':')

            if cmd == 'emit':
                emit = True

            fn = getattr(uinput, fn)
            cmd = getattr(device, cmd)
            value = int(value)
            syn = bool(syn)

            if emit:
                fn(cmd, value, syn)
            else:
                fn(cmd, syn)