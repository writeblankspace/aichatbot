import random
import discord
from discord.ext import commands
from f.cooldown import cooldown_cmd
from f.build_msg import build_msg, Reply_Bias
from f._dict import d, search_synonyms
from f.funcs import *
import asyncio

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
		split_message = message.split(" ")

		# if message contains cortana
		# this means the user wants to talk to cortana
		trigger = "cory"
		if trigger in split_message:
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
				elif has_phrase_with_combo(message, [[trigger], d["questions"]]) and \
					"?" in message:
					# if the message is a yes/no/maybe/idk question
					# and ends with a question mark
					bias = Reply_Bias()
					# the outcome will be found from the bias
					bias = bias.outcome
					# can be "good", "bad", "neutral", or "meh"
					# so outcomes can be synonyms of yes, no, idk and maybe
					if bias == "good":
						response = build_msg("yes")
					elif bias == "bad":
						response = build_msg("no")
					elif bias == "neutral":
						response = build_msg("maybe")
					elif bias == "meh":
						choice = random.choice(["meh", "idk"])
						response = build_msg(choice)
				elif common_data(split_message, search_synonyms("hi")):
					# if the message contains a form of 'hi'
					# it could be any synonym of hi
						responses = [
							f"hi",
							f"how are you",
							f"are you alright"
						]
						response = random.choice(responses)
				else:
					if randint(1, 5) == 1:
						responses = [
							"well how did you know I was lurking",
							"hey how are you",
							"B)",
							"hey",
							"yes ? I'm listening."
						]
						response = random.choice(responses)
					else:
						response = None
				
				# build the message
				if response != None:
					response = build_msg(response)
					# wait random amount of time
					await asyncio.sleep(randint(1, 3))
					await msg.reply(response)
		

def setup(bot):
	bot.add_cog(ai(bot))