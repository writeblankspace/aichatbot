import random
import discord
from discord.ext import commands
from f.cooldown import cooldown_cmd
from f.build_msg import build_msg
from f._dict import d, search_synonyms
from f.funcs import *

synonyms = d["synonyms"]

randint = random.randint

class ai(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	# bot's ai
	@commands.Cog.listener('on_message')
	async def ai(self, ctx, *, message: str = ""):
		lvlup_cooldown = cooldown_cmd(10, 2, "channel")
		bucket = lvlup_cooldown.get_bucket(ctx)
		retry_after = bucket.update_rate_limit()

		message = message.content.lower()

		# if message contains cortana
		# this means the user wants to talk to cortana
		if "cortana" in message:

			if retry_after:
				# if there's a cooldown, do this
				responses = [
					f"Look, I'm not that fast. Wait {retry_after} seconds.",
					f"Be patient gurl. Wait {retry_after} seconds.",
					f"If you think I'm fast, you're wrong. Wait {retry_after} seconds.",
				]
				response = random.choice(responses)
			# if there's no cooldown, do this
			# now this is where the fun begins :)
			# prepare for a marathon of if statements
			else:
				# if the message contains a form of 'hi'
				# it could be any synonym of hi
				# look for the list that contains 'hi' in synonyms
				hi_synonyms = search_synonyms("hi")
				# see if the message contains any of the synonyms
				if common_data(message, hi_synonyms):
					responses = [
						f"hi",
						f"how are you",
						f"are you alright"
					]
					response = random.choice(responses)
			
			# build the message!
			response = build_msg(response)

			await ctx.reply(response)


def setup(bot):
	bot.add_cog(ai(bot))