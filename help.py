import asyncio

import discord
from discord.ext import commands


class BotHelp(commands.HelpCommand):
    def __init__(self):
        super().__init__()