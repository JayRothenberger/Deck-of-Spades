import time
import uinput
import ctypes
import os
from PIL import Image, ImageOps
from demo import load_model, draw_and_return_ocr
from dino_model import dino_model, dino_transforms
# https://stackoverflow.com/questions/69645/take-a-screenshot-via-a-python-script-on-linux
LibName = os.path.abspath('/vagrant/printscrn/prtscn.so')
AbsLibPath = LibName
grab = ctypes.CDLL(AbsLibPath)

def grab_screen(x1,y1,x2,y2):
    w, h = x2-x1, y2-y1
    size = w * h
    objlength = size * 3

    grab.getScreen.argtypes = []
    result = (ctypes.c_ubyte*objlength)()

    grab.getScreen(x1,y1, w, h, result)
    return Image.frombuffer('RGB', (w, h), result, 'raw', 'RGB', 0, 1)

# imagepath = os.path.abspath('/vagrant/')

def main():
    DINOv2 = dino_model()
    DINOv2_transform = dino_transforms()
    events = (
        uinput.REL_X,
        uinput.REL_Y,
        uinput.BTN_LEFT,
        uinput.BTN_RIGHT,
        uinput.KEY_1,
        uinput.KEY_2,
        uinput.KEY_W,
        uinput.KEY_A,
        uinput.KEY_S,
        uinput.KEY_D,
        )
    time.sleep(10)
    print('starting test')
    with uinput.Device(events) as device:
        time.sleep(1)
        device.emit_click(uinput.BTN_LEFT)
        time.sleep(1)
        device.emit_click(uinput.KEY_1)
        time.sleep(1)
        device.emit_click(uinput.KEY_1)
        time.sleep(1)
        device.emit_click(uinput.KEY_1)
        time.sleep(1)
        im = grab_screen(0,0,800,600)
        im.save('/vagrant/screenshot0.png')
        for i in range(50):
            # syn=False to emit an "atomic" (5, 5) event.
            device.emit(uinput.REL_X, 10, syn=False)
            device.emit(uinput.REL_Y, -10)

            # Just for demonstration purposes: shows the motion. In real
            # application, this is of course unnecessary.
            time.sleep(0.1)

        im = grab_screen(0,0,800,600)

        model, mapper, transform, collator = load_model()

        img = ImageOps.exif_transpose(im).convert("RGB")

        coords, texts, img_out = draw_and_return_ocr(model, img, transform, collator)

        img_out.save('/vagrant/screenshot_labeled.png')
        im.save('/vagrant/screenshot1.png')
        start = time.time()
        out = DINOv2.forward_features(DINOv2_transform(img_out).unsqueeze(0))
        print(time.time() - start)
        print([key for key in out.keys()])

if __name__ == "__main__":
    main()