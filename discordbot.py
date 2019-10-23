from discord.ext import commands
from discord.ext import tasks
from datetime import datetime
import os
import traceback
bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']
CHANNEL_ID = 633125958848610308 #チャンネルID

#投稿する日時
dateTimeList = [
'2019/10/23 19:30',
'2019/10/23 19:40',
'2019/10/23 19:50',
'2019/10/23 20:00',
'2019/10/23 20:10',
'2019/10/23 20:20',
'2019/10/23 20:30'
]

# 60秒に一回ループ
@tasks.loop(seconds=60)
async def loop():
    # 現在の時刻
    now = datetime.now().strftime('%H:%M')
    if now == '21:15':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('おはよう')  

# 指定時間に走る処理
async def SendMessage():
    channel = client.get_channel(CHANNEL_ID)
    await channel.send('時間だよ')

@bot.event
async def on_command_error(ctx, error):
    await ctx.send(str(error))

@bot.event
async def on_message(message):
    # do some extra stuff here
    await bot.process_commands(message)

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

bot.run(token)

