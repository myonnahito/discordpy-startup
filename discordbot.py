from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def on_command_error(ctx, error):
    await ctx.send(str(error))


@bot.command()
async def ping(ctx):
    await ctx.send('pong')

@bot.command()
async def ねこ(ctx):
    await ctx.send('にゃーん')
    
#coding:UTF-8
import discord
from datetime import datetime
from discord.ext import tasks

TOKEN = "**********" #トークン
CHANNEL_ID = ********** #チャンネルID
# 接続に必要なオブジェクトを生成
client = discord.Client()


#投稿する日時
dateTimeList = [
'2019/10/22 17:00',
'2019/10/22 18:00',
'2019/10/22 19:00',
'2019/10/22 20:00',
'2019/10/22 21:00',
'2019/10/22 22:00',
'2019/10/22 23:00',
]

# 起動時に動作する処理
@client.event
async def on_ready():
    print('ready')

# 指定時間に走る処理
async def SendMessage():
    channel = client.get_channel(CHANNEL_ID)
    await channel.send('時間だよ')

# 30秒に一回ループ
@tasks.loop(seconds=30)
async def time_check():
    sleepTime = 0
    # 現在の時刻
    now = datetime.now().strftime('%Y/%m/%d %H:%M')
    if now in dateTimeList :
        print(now)
        await SendMessage()
        #該当時間だった場合は２重に投稿しないよう３０秒余計に待機
        await asyncio.sleep(30)

# メッセージ受信時に動作する処理
@client.event
async def on_message(message):
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return
    # 使用できるコマンド一覧
    if message.content == '!help':
        await message.channel.send('現在使用できるコマンドはありません')

#ループ処理
time_check.start()
# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)

    
    
    
bot.run(token)
