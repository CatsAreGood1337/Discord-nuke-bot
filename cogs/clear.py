from discord.ext import commands

class User(commands.Cog):

	def __init__(self, client):
		self.client = client

	@commands.Cog.listener()
	async def on_ready(self):
		pass

	@commands.command()
	async def clear(self, ctx, amount=1):
		await ctx.channel.purge(limit=amount)
		if amount == 1:
			print(f"{amount} message deleted")
		else:
			print(f"{amount} messages deleted")
			
def setup(client):
	client.add_cog(User(client))