# Discord.py is smoooooooooooooosh!!!!!
import discord
from discord.ext import commands
import asyncio

import pymongo
import os
import argparse
import collections


class Admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_guild_permissions(administrator=True)
    async def advicecard(self, ctx, member: discord.Member):
        pass

    @commands.command()
    @commands.has_guild_permissions(administrator=True)
    async def strike(self, ctx, member: discord.Member):
        pass

    @commands.command()
    @commands.has_guild_permissions(administrator=True)
    async def kick(self, ctx, member: discord.Member):
        pass

    @commands.command()
    @commands.has_guild_permissions(administrator=True)
    async def softban(self, ctx, member: discord.Member):
        pass

    @commands.command()
    @commands.has_guild_permissions(administrator=True)
    async def ban(self, ctx, member: discord.Member):
        pass

    @commands.command()
    @commands.has_guild_permissions(administrator=True)
    async def globalban(self, ctx, member: discord.Member):
        pass

    @commands.command()
    @commands.has_guild_permissions(administrator=True)
    async def rolelist(self, ctx, *roles: discord.Role):
        rolemembers = []
        for role in roles:
            rolemembers += [x.mention for x in role.members]
        rolemembers = [
            x for x, y in collections.Counter(rolemembers).items()
            if y == len(roles)
        ]
        if not rolemembers:
            embed = discord.Embed(title="見つかりませんでした。",
                      description="条件に当たる人が見つかりませんでした",
                      color=0xff0000)
            await ctx.send(embed=embed)
            break
        embed = discord.Embed(title="メンバー一覧",
                              description=', '.join(rolemembers),
                              color=0xeeeeee)
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Admin(bot))
