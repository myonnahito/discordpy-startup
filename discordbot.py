from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def on_command_error(ctx, error):
    await ctx.send(str(error))

@.event
client.on('message', message =>
{
  if(message.isMemberMentioned(client.user))
  {
    message.reply( '呼びましたか？' );
    return;
  }
});

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
