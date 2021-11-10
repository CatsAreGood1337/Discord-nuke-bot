import discord, asyncio
from asyncio import sleep
from discord.ext import commands
from colorama import init, Fore, Back, Style

class OnReady(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        	await self.client.change_presence(status=discord.Status.invisible, activity=discord.Game(" | *help"))
        	await sleep(15)

init()
print(Fore.GREEN + "Nuke-bot is online")
def setup(client):
    client.add_cog(OnReady(client))
