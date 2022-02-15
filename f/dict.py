import json

# read json file and turn into dict
with open("dictionary.json", 'r') as f:
	d = json.load(f)