from discord.ext import commands
import os
import traceback
from datetime import datetime
bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']
CHANNEL_ID = 一般 #チャンネルID
# 接続に必要なオブジェクトを生成
client = discord.Client()


#投稿する日時
dateTimeList = [
'2019/10/22 21:00',
'2019/10/22 21:01',
'2019/10/22 21:02',
'2019/10/22 21:03',
'2019/10/22 21:04',
'2019/10/22 21:05',
'2019/10/22 21:06'
]

# 起動時に動作する処理
@client.event
async def on_ready():
    print('ready')

# 指定時間に走る処理
async def SendMessage():
    channel = client.get_channel(CHANNEL_ID)
    await channel.send('時間だよ')

@bot.event
async def on_command_error(ctx, error):
    await ctx.send(str(error))


@bot.command()
async def ping(ctx):
    await ctx.send('pong')

bot.run(token)

