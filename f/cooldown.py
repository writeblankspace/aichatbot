from discord.ext import commands


def cooldown_cmd(rate, per, type):
	""" **Adds a cooldown to the command** \n
	rate = how many times user can use the command \n
	per = the cooldown in seconds \n
	type = the type of cooldown \n
	**Add the following code to command:**\n 
	```
	cooldown = cooldown_cmd(rate, per, type)
	bucket = message_cooldown.get_bucket(message/ctx)
	retry_after = bucket.update_rate_limit()

	if retry_after:
		pass # if there's a cooldown, do this
	else:
		pass # if there's no cooldown, do this
	```
	"""
	cooldown = commands.CooldownMapping

	if type == "default":
		return cooldown.from_cooldown(rate, per, commands.BucketType.default)
	if type == "user":
		return cooldown.from_cooldown(rate, per, commands.BucketType.user)
	if type == "guild":
		return cooldown.from_cooldown(rate, per, commands.BucketType.guild)
	if type == "channel":
		return cooldown.from_cooldown(rate, per, commands.BucketType.channel)
	if type == "member":
		return cooldown.from_cooldown(rate, per, commands.BucketType.member)
	if type == "category":
		return cooldown.from_cooldown(rate, per, commands.BucketType.category)
	if type == "role":
		return cooldown.from_cooldown(rate, per, commands.BucketType.role)
