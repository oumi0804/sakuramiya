import discord
from discord.ext import commands
from flask import Flask, redirect, url_for
from flask_discord import DiscordOAuth2Session, Unauthorized

import asyncio
import sys
import os
import traceback
from colorama import Fore, Back, Style

import config


class SAKURANOMIYA(commands.Bot):
    def __init__(self, command_prefix, cogs, **options):
        # スーパークラスのコンストラクタに値を渡して実行。
        super().__init__(command_prefix, **options)
        # cogフォルダにある.pyファイルを読み込む。
        for cog in os.listdir(f'./{cogs}'):
            if cog.endswith('.py'):
                try:
                    self.load_extension(f'{cogs}.{cog[:-3]}')
                    print(f"{cog}は正常にロードされました。")
                except Exception:
                    traceback.print_exc()

    async def on_ready(self):  # 準備完了時に呼び出す。
        print("準備完了しました。")
        if config.IS_DEBUG:
            print(f"{Style.DIM}[DEBUGGING NOW!]{Style.RESET_ALL}")
        print(f"{Style.DIM} ユーザー名:{self.user.name}")
        print(f" ユーザーID:{self.user.id}")
        print(f" Discord.pyのバージョン:{discord.__version__}")
        print(f" Pythonのバージョン:{sys.version}{Style.RESET_ALL}")
        await self.change_presence(activity=discord.Game(
            name=f'{self.command_prefix}￤{self.user.name} - by.amazakura0804'))

if __name__ == '__main__':
    sakuranomiya = SAKURANOMIYA("sa!", "cogs", intents=discord.Intents.all())
    sakuranomiya.run(config.DISCORD_TOKEN)