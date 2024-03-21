import io
import pyautogui
from base64 import b64encode
import requests
import key_api

KEY_IMG_BB = key_api.img_bb
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
print(res.status_code)