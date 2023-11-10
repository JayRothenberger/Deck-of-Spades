import asyncio, asyncvnc
from PIL import Image
import time

async def run_client():
    async with asyncvnc.connect('localhost', 5901, password='vncpassword') as client:
        print(client)
        # Retrieve pixels as a 3D numpy array
        pixels = await client.screenshot()
        
        # Save as PNG using PIL/pillow
        image = Image.fromarray(pixels)
        image.save('screenshot.png')

asyncio.run(run_client())