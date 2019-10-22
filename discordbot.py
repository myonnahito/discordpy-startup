from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']
TOKEN = "NjM2MDk2MTk5ODE1ODU2MTM4.Xa6pMQ.mYGDj9YcCGgdVi_CZqoyo39MvVo" #トークン
CHANNEL_ID = "一般" #チャンネルID

#投稿する日時
dateTimeList = [
'2019/10/22 20:10',
'2019/10/22 20:11',
'2019/10/22 20:12',
'2019/10/22 20:13',
]

@bot.event
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

@bot.command()
async def neko(ctx):
    await ctx.send('にゃーん')

@bot.command()
async def w(ctx):
    await ctx.send('草生やすな')

@bot.command()
async def ww(ctx):
    await ctx.send('ダブルの衝撃ｗ')

bot.run(token)
