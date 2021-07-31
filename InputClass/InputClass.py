import os
import sys
import discord
import asyncio
from discord.ext import commands
from discord.ext.commands import has_role
from discord.utils import get

sys.path.append('../')

class InputClass(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        # removes the default help
        self.bot.remove_command('help')


    @commands.command()
    async def kiss(self, ctx):
        user = ctx.author
        response = "I love Thelma Lily Eden and Linds!"
        await ctx.send(response)
def setup(bot):
    bot.add_cog(InputClass(bot))