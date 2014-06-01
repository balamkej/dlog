#!/usr/bin/env python3

import argparse, json

try:
    with open('dlog.json') as file:
        pass
except IOError as e:
    print('Unable to find (or perhaps read) your Daily Log file. Use the --init flag to create a new one.')

parser = argparse.ArgumentParser(description='Daily Log App')

group = parser.add_mutually_exclusive_group()

# Define a series of flags and assign them to a mutually exclusive group: 
# --init stores True in var init_switch, else False
# -i appends an int to the list in var increment. We allow multiple -i flags, e.g., -i book -i "book review" -i "journal article"
# -a appends a string to the list in var project. We allow multiple -a flags, e.g., -a book -a "book review" -a "journal article"
# -s stores exactly two int arguments as list in var swap 

group.add_argument('--init', action="store_true", dest='init_switch', default=False)
group.add_argument('-i', action='append', dest='increment', type=int)
group.add_argument('-a', action='append', dest='projects')
group.add_argument('-s', nargs=2, action='store', dest='swap', type=int)

results = parser.parse_args()

print('init_switch=', results.init_switch)
print('increment=', results.increment)
print('projects=', results.projects)
print('swap=', results.swap)

# Touch dlog.json and write to it a json object
def init():
	f = open('dlog.json', 'w')
	data = {"projects":[]}
	json.dump(data, f)
	f.close()

def add():
	pass

def increment():
	pass

def swap():
	pass

# Some example json
# {
# "projects": [
# { "title":"JoS Review" , "count":14 , "init_date":"Feb 1 2014" }, 
# { "title":"Mayan semantics review article" , "count":40 , "init_date":"Mar 15 2014" }, 
# { "title":"Swarms" , "count":3 , "init_date":"May 15 2014" }
# ]
# }