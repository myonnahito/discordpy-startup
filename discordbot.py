from discord.ext import commands
from datetime import datetime
import os
import traceback
bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']
CHANNEL_ID = 一般 #チャンネルID

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

@bot.event
async def on_command_error(ctx, error):
    await ctx.send(str(error))


@bot.command()
async def ping(ctx):
    await ctx.send('pong')

bot.run(token)

