import asyncio, asyncvnc
from PIL import Image
import time
import socket

UDP_IP = "127.0.0.1"
UDP_PORT = 5005
SOCK = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP


def socket_toem(cmd):
    SOCK.sendto(cmd.encode(), (UDP_IP, UDP_PORT))


async def run_client():
    async with asyncvnc.connect('localhost', 5901, password='vncpassword') as client:

        # Retrieve pixels as a 3D numpy array
        pixels = await client.screenshot()
        
        # Save as PNG using PIL/pillow
        image = Image.fromarray(pixels)
        image.save('screenshot0.png')
        client.keyboard.write('111')

        with client.keyboard.hold('Tab'):
            pixels = await client.screenshot()
            # Save as PNG using PIL/pillow
            image = Image.fromarray(pixels)
            image.save('screenshot0.png')

        socket_toem('REL_X:emit:-50:False')
        socket_toem('REL_Y:emit:-50:True')

        with client.keyboard.hold('Tab'):
            pixels = await client.screenshot()
            # Save as PNG using PIL/pillow
            image = Image.fromarray(pixels)
            image.save('screenshot1.png')

asyncio.run(run_client())