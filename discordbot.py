from discord.ext import commands
from discord.ext import tasks
from datetime import datetime
import os
import traceback
bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']
CHANNEL_ID = 633125958848610308 #チャンネルID

@bot.command()
async def echo(ctx, *, message: str):
    await ctx.send(message)

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
@bot.command()

async def タクティパンツ(ctx):
    await ctx.send('ｱｰｯｱｯｱｯｱｯﾊｯﾊｯﾊｯﾎｯﾊｯﾎｯﾎｯﾎｯﾎｰｩﾎｰｩﾎｰｩﾎｰｩﾎｫｫｰ!!ﾌｫｰｯﾌﾌｫｰｯﾌﾌｫｰｯﾌﾌｫｰｫｫｫｫｫ!!ﾌｫｰｯﾊｯｱﾊﾌｯﾊｯﾊｯﾊｯﾊ!!ﾄﾞﾝﾄﾞﾝﾊﾟﾁﾊﾟﾁﾊﾟﾁﾊﾟﾁﾊﾟﾁｫﾌｧｯﾌｫｯﾊｯﾊｯ!!ﾊﾋﾋﾍﾊﾌﾊｧﾄﾞﾝﾄﾞﾝﾄﾞﾝﾄﾞﾝ!!')
    @bot.command()
    
async def 螺旋の念(ctx):
    await ctx.send('ｵｰｯ↓ﾎｯﾎｯﾎｯﾌﾎｯﾎﾌﾎﾌﾎﾌ↑ﾎﾊﾎｯﾊｯﾎｯﾎｯﾊｯﾊ(ﾄﾞﾝﾄﾞﾝﾄﾞﾝﾄﾞﾝﾄﾞﾝ)ｳﾎｳﾌﾎｳﾎﾎ↓ﾎﾎｳﾎｳﾎﾎ(ﾄﾞﾝﾄﾞﾝﾄﾞﾝ)ｳｯﾎｯﾎｯﾎ(ﾊﾞﾀﾝﾊﾞﾀﾝ)ﾊｯﾊｯﾊｯﾊｯｱﾊｯｱﾊｯ(ﾊﾞﾀﾝ)ﾊｯﾊｱﾊｯｯﾊｯﾊｯｱﾊ出たwww出たっ出た出た(ﾄﾞﾝ)ｯﾊｯﾊｯﾊｯﾊｗｗｗｱｯﾊｧ出たwwwwﾓｳｯﾎｫｯﾊｯﾊｯﾊｯﾊｯﾊｯﾊwww出たwww(ﾄﾞﾝ)wwwwwwｱｯﾊｧww出たwwwwwｯﾊｧｯﾊwwwww出たwwwwww出たｯﾊｯﾊｱｯﾊｯﾊwwww出たぁww出ったぁwwwwwwﾎﾝﾄwwwﾃﾞﾀwwwwwwwwﾌｧｰｯﾊｱやったぁwwwwwwﾊｰｯﾊﾊｯﾊwww本当にもうwwwwwwwｯﾊｯﾊｯﾊﾊｯﾊww
(ｶﾞﾀﾝ)ｱｲﾀﾞﾀﾞﾀﾞﾀﾞ今ｯ (ｶﾞﾝｯｶﾞﾝ)ｱｲｯﾀﾞ...ちょっｱｯｯ ｱﾊｱｧ痛ってぇ... ｱｧ...ﾊｧｧ')
    @bot.command()
                   
async def さもさん(ctx):
    await ctx.send('よっちゃｗ')
    @bot.command()
async def 決闘(ctx):
    await ctx.send('ディメ禁止')
    @bot.command()
                   
async def 卍解(ctx):
    await ctx.send('故に侘助')
    @bot.command()
                   
async def 連絡(ctx):
    await ctx.send('@everyoneイシス出席表 明日までに記入してくださいね')
    @bot.command()
                   
async def 締め切り(ctx):
    await ctx.send('@everyoneイシス出席 締め切りだからね')
    @bot.command()
                   
async def アラド戦記(ctx):
    await ctx.send('13年だって')
    @bot.command()
                   
async def 美濃加茂(ctx):
    await ctx.send('そうかもｗ')
    @bot.command()
                   
async def 山田(ctx):
    await ctx.send('太郎ｗ')
    @bot.command()
                   
async def 詠唱1(ctx):
    await ctx.send('天光満る処に我は在り、黄泉の門開く処に汝在り、出でよ神の雷')
    @bot.command()
                   
async def 詠唱2(ctx):
    await ctx.send('消えなさい！旋律の戒めよ！死霊使い（ネクロマンサー）の名の下に具現せよ！ミスティック・ケージ！！
力というものを思い知りなさい！')
    @bot.command()
                   
async def foo(ctx):
    await ctx.send('Hello')
    @bot.command()

bot.run(token)

