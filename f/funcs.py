# if there is a common word in the message and the synonyms
from typing import List
import itertools

def common_data(list1, list2):
	""" returns true if both lists have something in common
	"""
	result = False
	# traverse in the 1st list
	for x in list1:
		# traverse in the 2nd list
		for y in list2:
			# if one common
			if x == y:
				result = True
				return result 
	return result

def all_combos(list_of_combos: list):
	""" returns all possible combinations in a list of lists
	e.g. [[1, 2], [3, 4]] -> ["1 3", "1 4", "2 3", "2 4"]
	"""
	result = []
	# find the longest list in list_of_combos
	longest = max(list_of_combos, key=len)
	for i in range(len(longest) * (len(list_of_combos) - 1)):
		result.append([])
	for i in list_of_combos:
		iterator = 0
		# get all combinations of the list
		for j in i:
			# add to the result
			for k in range(round(len(longest) / len(i))):
				result[iterator].append(j)
				iterator += 1
	return result

def has_phrase(message: str, phrases: list):
	""" returns true if the message contains one of the phrases
	e.g. phrase = [["hey", "world"], ["hello", "world"]]
	"""
	result = False
	for i in phrases:
		# if message contains it
		i = " ".join(i)
		if i in message:
			result = True
			return result

def has_phrase_with_combo(message: str, list_of_combos: list):
	""" mix of has_phrase() and all_combos()
	"""
	return has_phrase(message, all_combos(list_of_combos))