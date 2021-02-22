import discord
from discord.ext import commands, tasks
from flask import Flask, redirect, url_for
from flask_discord import DiscordOAuth2Session, Unauthorized

import asyncio
import sys
import os
import traceback
from colorama import Fore, Back, Style

import config
intents=discord.Intents.all()

def command_prefix():
	pass

async def status_chenge(self):
	status_massages = config.STATUS_MESSAGE
	sleeptime = config.STATUS_CHANGE_TIME
	while True:
		if len(status_massages) == 1:
			await app.change_presence(activity=discord.Game(eval(status_massage)))
			await asyncio.sleep(sleep_time)
			continue
		for status_massage in status_massages:
			await self.change_presence(activity=discord.Game(eval(status_massage)))
			await asyncio.sleep(sleeptime)

class SAKURANOMIYA(commands.Bot):
	def __init__(self, **options):
		# スーパークラスのコンストラクタに値を渡して実行。
		super().__init__(command_prefix=command_prefix, intents=intents, **options)
		# cogフォルダにある.pyファイルを読み込む。
		for cog in os.listdir(f'./cogs'):
			if cog.endswith('.py'):
				try:
					self.load_extension(f'cogs.{cog[:-3]}')
					print(f"[cogs] {cog}は正常にロードされました。")
				except Exception:
					traceback.print_exc()

	async def on_ready(self):  # 準備完了時に呼び出す。
		print("[ready] 準備完了しました。")
		if config.IS_DEBUG:
			print(f"{Style.DIM}[DEBUGGING NOW!]{Style.RESET_ALL}")
		print(f"{Style.DIM} ユーザー名:{self.user.name}")
		print(f" ユーザーID:{self.user.id}")
		print(f" Discord.pyのバージョン:{discord.__version__}")
		print(f" Pythonのバージョン:{sys.version}{Style.RESET_ALL}")

		embed = discord.Embed(title='Botが起動しました。', color=0x00ff00)
		app = await self.application_info()
		await app.owner.send(embed=embed)
		await self.loop.create_task(status_chenge(self))

	async def on_closed(self):  # 準備完了時に呼び出す。
		embed = discord.Embed(title='Botが停止しました。', color=0xff0000)
		self.get_user(self.owner_id).send(embed=embed)

	async def on_command_error(self, ctx, error):
		ignore_errors = (
			BadArgument,
			CheckFailure,
			CommandNotFound,
        )
		if isinstance(error, ignore_errors):
			return
		embed = discord.Embed(title='error!', description=f'```{error}```', color=0xff0000)
		await ctx.send(embed=embed)
    

if __name__ == '__main__':
	sakuranomiya = SAKURANOMIYA()
	sakuranomiya.run(config.DISCORD_TOKEN)