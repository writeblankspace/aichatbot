# these functions help build the message
# they use the dictionary to randomise the response with synonyms

# dictionary
from f._dict import d
from f.handle_references import handle_references
import random
randint = random.randint

# adds bias to the message. The response can be either good or bad, or neutral
# this isn't useful... yet
class Reply_Bias:
	def __init__(self, good: int = 1, bad: int = 1, neutral: int = 1, meh: int = 1):
		self.good = good
		self.bad = bad
		self.neutral = neutral
		self.meh = meh
		self.outcome = self.find_outcome()
	
	def find_outcome(self):
		outcomelist = []
		for i in range(self.good):
			outcomelist.append("good")
		for i in range(self.bad):
			outcomelist.append("bad")
		for i in range(self.neutral):
			outcomelist.append("neutral")
		for i in range(self.meh):
			outcomelist.append("meh")
		
		return random.choice(outcomelist)


def build_msg(msg, use_append: bool = True, use_synonyms: bool = True, synonyms: list = d["synonyms"]):
	""" Builds the message using `msg`. Spaces will be added automatically.
	If `use_append` is set to True, the message will be appended with a random value from the `_append` dictionary.
	If `use_synonyms` is set to True, synonyms will be used using the dictionary"""

	if type(msg) == str:
		msg = msg.split(" ")
	
	
	# if use_append is True, add a random value from the _append dictionary
	if use_append:
		rand = randint(1, 7)
		if rand == 1:
			# e.g. "bruh the quick brown fox jumps over the lazy dog"
			random_append = random.choice(d["_append"]["all"])
			new = []

			new.append(random_append)
			for word in msg:
				new.append(word)
		elif rand == 2:
			# e.g. "the quick brown fox jumps over the lazy dog bruh"
			random_append = random.choice(d["_append"]["all"])
			new = []

			for word in msg:
				new.append(word)
			new.append(random_append)
		elif rand == 3:
			# e.g. "i- the quick brown fox jumps over the lazy dog"
			random_append = random.choice(d["_append"]["all_prefixes"])
			new = []

			new.append(random_append)
			for word in msg:
				new.append(word)
		elif rand == 4:
			# e.g. "the quick brown fox jumps over the lazy dog ..."
			random_append = random.choice(d["_append"]["all_suffixes"])
			new = []

			for word in msg:
				new.append(word)
			new.append(random_append)
		elif rand in [5, 6, 7]:
			# e.g. "the quick brown fox jumps over the lazy dog"
			# nothing happens
			new = msg
		
		msg = new
		

	if use_synonyms:
		new_msg = []

		for i in msg:
			# synonyms is a list of lists, where each list is a list of words that are synonyms for each other
			# if that doesn't make sense, then don't make sense of it
			synonym_found = False
			for j in synonyms:
				if i in j:
					# if word is in that synonym list
					# choose a random synonym
					synonym = random.choice(j)
					# replace the word with the synonym
					new_msg.append(synonym)
					synonym_found = True
					break
			if not synonym_found:
				new_msg.append(i)
	else:
		new_msg = msg

	joined = " ".join(new_msg)
	# remove spaces before punctuation
	for i in [".", ",", "!", "?"]:
		joined = joined.replace(f" {i}", f"{i}")

	return joined



