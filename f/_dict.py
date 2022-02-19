import json
from handle_references import handle_references

# read json file and turn into dict
with open("_dictionary.json", 'r') as f:
	d = json.load(f)

# there are @ references in this list of lists
# so we must handle them
new_obj = []
for i in d["synonyms"]:
	i = handle_references(i)
	new_obj.append(i)
d["synonyms"] = new_obj

# get all of the _append stuff
all = []
all_prefixes = []
all_suffixes = []

# get keys in d["_append"]
keys = d["append"].keys()

for key in keys:
	if key.endsWith("_prefix"):
		# add values of the key to all_prefixes
		all_prefixes.extend(d["append"][key])
	elif key.endsWith("_suffix"):
		# add values of the key to all_suffixes
		all_suffixes.extend(d["append"][key])
	else:
		# add values of the key to all
		all.extend(d["append"][key])

# ily github copilot <3

d["_append"]["all"] = all
d["_append"]["all_prefixes"] = all_prefixes
d["_append"]["all_suffixes"] = all_suffixes

# search for the synonym list
# e.g. if you want a list of synonyms for 'hi'
def search_synonyms(word: str):
	for i in d["synonyms"]:
		if word in i:
			hi_synonyms = i
			break
	return hi_synonyms