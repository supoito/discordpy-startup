from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


@bot.command()
async def ping(ctx):
    await ctx.send('pong/n pong')


bot.run(token)
import gspread
import json

#ServiceAccountCredentials：Googleの各サービスへアクセスできるservice変数を生成します。
from oauth2client.service_account import ServiceAccountCredentials 

#2つのAPIを記述しないとリフレッシュトークンを3600秒毎に発行し続けなければならない
scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']

#認証情報設定
#ダウンロードしたjsonファイル名をクレデンシャル変数に設定（秘密鍵、Pythonファイルから読み込みしやすい位置に置く）
credentials = ServiceAccountCredentials.from_json_keyfile_name('asarikokuti-6bb0166725e7.json', scope)

#OAuth2の資格情報を使用してGoogle APIにログインします。
gc = gspread.authorize(credentials)

#共有設定したスプレッドシートキーを変数[SPREADSHEET_KEY]に格納する。
SPREADSHEET_KEY = '1p5NK1hgzI17CtnI8-CQqC7GzRMhwWgT3zc41S_N3zpw'

worksheet = workbook.sheet1

#共有設定したスプレッドシートのシート1を開く
worksheet = gc.open_by_key(SPREADSHEET_KEY).sheet1

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
