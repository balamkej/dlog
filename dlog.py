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

# Check that var title is not a title in the daily log, else add it.
def add(title):
    f = open('dlog.json', 'r')
    data = json.load(f)
    f.close()

    titles = []
    for i in data['projects']:
        titles.append(i['title'])

    if title in titles:
        print('You already have the project called \"%s\" in your Daily Log.' % (title))
    else:
        data['projects'].append({ "title":title , "count":0 })   
        f = open('dlog.json', 'w')
        json.dump(data, f)
        f.close()

# Check that var index for the project is in the appropriate range, then increment the corresponding counter.
def increment(index):
    index = index - 1 # Shift index for Python
    f = open('dlog.json', 'r')
    data = json.load(f)
    f.close()

    data_len = len(data['projects'])

    if data_len == 0:
        print('You don\'t have any projects to increment.')
    elif data_len <= index or index < 0:
        print('Index is out of range.') 
    else:
        data['projects'][index]['count'] = data['projects'][index]['count'] + 1 
        f = open('dlog.json', 'w')
        json.dump(data, f)
        f.close()

# Check that the two indices are in range, then switch the positions of the corresponding projects in the project list
def swap(first, second):
    first = first - 1
    second = second - 1 # Shift indices for Python
    f = open('dlog.json', 'r')
    data = json.load(f)
    f.close()

    data_len = len(data['projects'])

    if data_len == 0:
        print('You don\'t have any projects to increment.')
    elif data_len <= first or first < 0:
        print('Your index %s is out of range.' % (first + 1))
    elif data_len <= second or second < 0:
        print('Your index %s is out of range.' % (second + 1))
    else:
        swap1 = data['projects'][first]
        swap2 = data['projects'][second]
        data['projects'][first] = swap2
        data['projects'][second] = swap1
        f = open('dlog.json', 'w')
        json.dump(data, f)
        f.close()

# Delete project at var index
def delete(index):
    index = index - 1
    f = open('dlog.json', 'r')
    data = json.load(f)
    f.close()

    data_len = len(data['projects'])

    if data_len == 0:
        print('You don\'t have any projects to increment.')
    elif data_len <= index or index < 0:
        print('Your index is out of range.')
    else:
        del data['projects'][index]
        f = open('dlog.json', 'w')
        json.dump(data, f)
        f.close()


# Some example json
# {
# "projects": [
# { "title":"JoS Review" , "count":14 }, 
# { "title":"Mayan semantics review article" , "count":40 }, 
# { "title":"Swarms" , "count":3 }
# ]
# }