# Dependencies
- pip intsall bs4
- pip install requests
- pip install pyautogui
    - arch wayland 환경에서는 동작하지 않음. X11환경에서만 동작
- pip install asyncio
- pip install aiogram
- pip install pandas

# 필요한 api :
### token_tellegram.py
- bot_token 에 텔레그램 채팅 봇의 토큰 (bot_father 사용)
- bot_chat_id 에 봇 채팅 id

### key_api.py
- img_bb 에 계정 생성 후 계정 api 발급받아 입력
- c2_url 에 워크스페이스 생성 후 http 서버의 주소 받아와 입력