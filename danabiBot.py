#coding:UTF-8
from datetime import datetime
from discord.ext import tasks

CHANNEL_ID = 一般 #チャンネルID
# 接続に必要なオブジェクトを生成
client = discord.Client()


#投稿する日時
dateTimeList = [
'2019/10/22 22:40',
'2019/10/22 22:50',
'2019/10/22 23:00',
'2019/10/22 23:05',
'2019/10/22 23:10',
'2019/10/22 23:20',
'2019/10/22 23:30',
]

# 指定時間に走る処理
async def SendMessage():
    channel = client.get_channel(CHANNEL_ID)
    await channel.send('時間だよ')
