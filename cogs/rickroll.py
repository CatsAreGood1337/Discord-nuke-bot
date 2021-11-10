from discord.ext import commands
import random
from colorama import init, Fore, Back, Style
class User(commands.Cog):

	def __init__(self, client):
		self.client = client

	@commands.Cog.listener()
	async def on_ready(self):
    init()
    pass

	@commands.command()
	async def rickroll(self, ctx):
		links = ['https://www.youtube.com/watch?v=dQw4w9WgXcQ',
				 'https://www.youtube.com/watch?v=S5o9g22BdXw',
				 'https://www.youtube.com/watch?v=iik25wqIuFo',
				 'https://www.youtube.com/watch?v=EE-xtCF3T94',
				 'https://www.youtube.com/watch?v=cvh0nX08nRw',
				 'https://www.youtube.com/watch?v=xm3YgoEiEDc',
				 'https://www.youtube.com/watch?v=IO9XlQrEt2Y']
		await ctx.send("<" + links[random.randint(0, len(links))] + ">")
    
		print(Fore.GREEN + f"Rickrolled")

def setup(client):
	client.add_cog(User(client))
