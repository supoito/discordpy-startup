
from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']

# イベント開催情報
event1_name = worksheet.acell('B2').value
event1_date = dt.strptime(worksheet.acell('B3').value, '%Y-%m-%d %H:%M:%S')
event1_medal = dt.strptime(worksheet.acell('B4').value, '%Y-%m-%d %H:%M:%S')
event2_name = worksheet.acell('D2').value
event2_date = dt.strptime(worksheet.acell('D3').value, '%Y-%m-%d %H:%M:%S')
event2_medal = dt.strptime(worksheet.acell('D4').value, '%Y-%m-%d %H:%M:%S')
# ガチャメダル引き換え期限
gacha1_name = worksheet.acell('B6').value
gacha1_expiry = dt.strptime(worksheet.acell('B7').value, '%Y-%m-%d %H:%M:%S')
gacha2_name = worksheet.acell('D6').value
gacha2_expiry = dt.strptime(worksheet.acell('D7').value, '%Y-%m-%d %H:%M:%S')


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


@bot.command()
async def ping(ctx):
    await ctx.send('pong')


bot.run(token)
