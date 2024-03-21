from crawler import *
import asyncio
from aiogram import Bot
import token_tellegram

CHAT_ID = token_tellegram.bot_chat_id
TEL_TOKEN = token_tellegram.bot_token

def getBTCUSD():
    yfc = YahooFinanceCrawler()
    result_list = yfc.get_result_data("BTC-USD", "2024/03/20", "2024/3/20")
    btcusd = result_list[0]["close_price"]
    return btcusd

def getBTCKRW():
    return 98760000


def getUSDKRW():
    yfc = YahooFinanceCrawler()
    result_list = yfc.get_result_data("KRW=X", "2024/03/20", "2024/3/20")
    usdkrw = result_list[0]["close_price"]
    return usdkrw

def calcKimPre():
    btcusd = getBTCUSD()
    usdkrw = getUSDKRW()
    btckrw = getBTCKRW()
    kimpre = 100 * (btckrw - btcusd * usdkrw) / (btcusd * usdkrw)
    return kimpre


async def sendMsg():
    bot = Bot(token=TEL_TOKEN)
    await bot.send_message(chat_id=CHAT_ID, text=("김프가 높음 : {:.2f}\n".format(kimpre)))
    await bot.close()

kimpre = calcKimPre()
if kimpre>5.0:
    asyncio.run(sendMsg())
    