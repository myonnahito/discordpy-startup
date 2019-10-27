from discord.ext import commands
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

bot.run(token)

