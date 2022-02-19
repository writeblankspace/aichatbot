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
	async def ai(self, msg):
		lvlup_cooldown = cooldown_cmd(10, 2, "channel")
		bucket = lvlup_cooldown.get_bucket(msg)
		retry_after = bucket.update_rate_limit()

		message = msg.content
		message = message.lower()

		# if message contains cortana
		# this means the user wants to talk to cortana
		if "cory" in message.split(" "):
			async with msg.channel.typing():

				print(f"+ listening: {message}")

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
				elif common_data(message, search_synonyms("hi")):
					# if the message contains a form of 'hi'
					# it could be any synonym of hi
						responses = [
							f"hi",
							f"how are you",
							f"are you alright"
						]
						response = random.choice(responses)
				else:
					responses = [
						"well how did you know I was lurking",
						"hey how are you",
						"👀",
						"shut up"
					]
					response = random.choice(responses)
				
				# build the message!g
				if response != None:
					response = build_msg(response)

					await msg.reply(response)
		

def setup(bot):
	bot.add_cog(ai(bot))