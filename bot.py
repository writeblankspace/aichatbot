# initiating bot
import os
import discord
from dotenv import load_dotenv
from discord.ext import commands
from f.alive import keep_alive
import random

# get .env secrets
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
OWNERS = os.getenv('OWNERS').split(", ")

# import cogs
initial_extensions = [
	"jishaku",
]

# rich presence
activity = discord.Activity(
	# TODO change the status every so often
	name="If the story's over, why am I still writing pages?",
	type=discord.ActivityType.listening
)

# Discord Intents settings
intents = discord.Intents.default()
intents.members = True
intents.presences = True

bot = commands.Bot(
	command_prefix=["c:", "c: "],
	activity=activity,
	status=discord.Status.idle,
	afk=False,
	intents=intents,
	strip_after_prefix=True,
	owner_ids=OWNERS,
	case_insensitive=True
)

# load extensions
if __name__ == '__main__':
	for extension in initial_extensions:
		bot.load_extension(extension)
		print(f"📥 {extension}")


@bot.event
async def on_ready():
	# print the bot's status
	randcode = random.randint(1000000, 9999999)
	print(f'{bot.user} has connected to Discord! [{randcode}]')
	print(f'Successfully logged in and booted...!')

# run the bot
keep_alive()
bot.run(TOKEN)