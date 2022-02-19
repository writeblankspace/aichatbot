def handle_references(d: dict, obj):
	""" Handles references in strings to other parts of the dict 
	e.g. "@_expressions.happy would be replaced with the value of that part of the dict 
	Returns a list of strings
	"""
	
	def handle_word(word):
		if word.startswith("@"):
			# it is a reference to a different part of the dict
			# remove the @ in the word
			word = word[1:]
			# split the word with a .
			# each part represents a 'dir'
			# e.g. @_expressions.happy
			# would be split into ["_expressions", "happy"]
			dirs = word.split(".")
			# go to the target dir
			# e.g. d["_expressions"]["happy"]
			# if the dir doesn't exist, return the original word
			current_dir = d
			for i in dirs:
				current_dir = current_dir.get(i)
				if current_dir is None:
					return word
					# the process stops here
					# so don't worry
		else:
			# it's not a reference; ignore it
			return word
	
	if isinstance(obj, list):
		# if obj is a list
		new_obj = []
		for i in obj:
			i = handle_word(i)
			new_obj.append(i)
	else:
		# if obj is a string
		new_obj = [handle_word(obj)]

	returning_obj = []

	# remove duplicates from new_obj
	for i in new_obj:
		if i not in returning_obj:
			returning_obj.append(i)

	return returning_obj