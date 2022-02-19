# if there is a common word in the message and the synonyms
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