# these functions help build the message
# they use the dictionary to randomise the response with synonyms

# dictionary
from f._dict import d
from f.handle_references import handle_references
import random
randint = random.randint

# adds bias to the message. The response can be either good or bad, or neutral
# this isn't useful... yet
class Bias:
	def __init__(self, good: int = 1, bad: int = 1, neutral: int = 1):
		self.good = good
		self.bad = bad
		self.neutral = neutral
		self.outcome = self.find_outcome()
	
	def find_outcome(self):
		outcomelist = []
		for i in range(self.good):
			outcomelist.append("good")
		for i in range(self.bad):
			outcomelist.append("bad")
		for i in range(self.neutral):
			outcomelist.append("neutral")
		
		return random.choice(outcomelist)


def build_msg(msg: list|str, use_append: bool = True, use_synonyms: bool = True, synonyms: list = d["synonyms"]):
	""" Builds the message using `msg`. Spaces will be added automatically.
	If `use_append` is set to True, the message will be appended with a random value from the `_append` dictionary.
	If `use_synonyms` is set to True, synonyms will be used using the dictionary"""

	if type(msg) == str:
		msg = msg.split(" ")
	
	# if use_append is True, add a random value from the _append dictionary
	if use_append:
		rand = randint(1, 6)
		if rand == 1:
			# e.g. "bruh the quick brown fox jumps over the lazy dog"
			random_append = random.choice(d["_append"]["all"])
			msg = [random_append].append(msg)
		elif rand == 2:
			# e.g. "the quick brown fox jumps over the lazy dog bruh"
			random_append = random.choice(d["_append"]["all"])
			msg = msg.append(random_append)
		elif rand == 3:
			# e.g. "i- the quick brown fox jumps over the lazy dog"
			random_append = random.choice(d["_append"]["all_prefixes"])
			msg = [random_append].append(msg)
		elif rand == 4:
			# e.g. "the quick brown fox jumps over the lazy dog ..."
			random_append = random.choice(d["_append"]["all_suffixes"])
			msg = msg.append(random_append)
		elif rand == 5 or rand == 6:
			# e.g. "the quick brown fox jumps over the lazy dog"
			# nothing happens
			pass

	if use_synonyms:
		new_msg = []

		for i in msg:
			# synonyms is a list of lists, where each list is a list of words that are synonyms for each other
			# if that doesn't make sense, then don't make sense of it
			for j in synonyms:
				if i in j:
					# choose a random synonym
					synonym = random.choice(j)
					# replace the word with the synonym
					new_msg.append(synonym)
					break
	else:
		new_msg = msg

	joined = " ".join(new_msg)
	# remove spaces before punctuation
	for i in [".", ",", "!", "?", ";", ":", "-"]:
		joined = joined.replace(f" {i}", f"{i}")

	return joined



