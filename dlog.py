#!/usr/bin/env python3

import argparse, json, sys, os

path = '/Users/rhenderson/Dropbox/code/dlog'
jsonfile = os.path.join(path, 'dailylog.json')
tick = '▇'
sad = u"\u2639"

try:
    with open(jsonfile) as file:
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
group.add_argument('-d', action='append', dest='delete', type=int)
group.add_argument('-a', action='append', dest='projects')
group.add_argument('-s', nargs=2, action='store', dest='swap', type=int)

results = parser.parse_args()

# Touch dlog.json and write to it a json object
def init():
    f = open(jsonfile, 'w')
    data = {"projects":[]}
    json.dump(data, f)
    f.close()

# Add title to the Daily Log unless already there
def add(title):
    f = open(jsonfile, 'r')
    data = json.load(f)
    f.close()

    titles = []
    for i in data['projects']:
        titles.append(i['title'])

    if title in titles:
        print('You already have the project called \"%s\" in your Daily Log.' % (title))
    else:
        data['projects'].append({ "title":title , "count":0 })
        f = open(jsonfile, 'w')
        json.dump(data, f)
        f.close()

# Increment the project counter associated with index.
def increment(index):
    index = index - 1 # Shift index for Python
    f = open(jsonfile, 'r')
    data = json.load(f)
    f.close()

    data_len = len(data['projects'])

    if data_len == 0:
        print('You don\'t have any projects to increment.')
    elif data_len <= index or index < 0:
        print('Index is out of range.')
    else:
        data['projects'][index]['count'] = data['projects'][index]['count'] + 1
        f = open(jsonfile, 'w')
        json.dump(data, f)
        f.close()

# Switch the position of two projects at the given indices
def swap(first, second):
    first = first - 1
    second = second - 1 # Shift indices for Python
    f = open(jsonfile, 'r')
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
        f = open(jsonfile, 'w')
        json.dump(data, f)
        f.close()

# Delete project at index
def delete(index):
    index = index - 1
    f = open(jsonfile, 'r')
    data = json.load(f)
    f.close()

    data_len = len(data['projects'])

    if data_len == 0:
        print('You don\'t have any projects to increment.')
    elif data_len <= index or index < 0:
        print('Your index is out of range.')
    else:
        del data['projects'][index]
        f = open(jsonfile, 'w')
        json.dump(data, f)
        f.close()

# Print dlog graph
def print_graph(label, title, count):
    print("{}: ".format(label), end="")
    if count == 0:
        sys.stdout.write(sad)
    else:
        for i in range(count):
            sys.stdout.write(tick)

    print("  {} [{} days]".format(title,count))



# If-block to call appropriate functions given command line flags.
if results.init_switch == True:
    init() # Run init() if --init flag is supplied
elif results.increment != None:
    for i in results.increment:
        increment(i) # Call increment() on each index supplied by -i flag
elif results.delete != None:
    for i in results.delete:
        delete(i) # Call delete() on each index supplied by -i flag
elif results.projects != None:
    for i in results.projects:
        add(i) # Call add() on each index supplied by -a flag
elif results.swap != None:
    first = results.swap[0]
    second = results.swap[1]
    swap(first,second) # Call swap() on the two argument supplied by -s flag. Note that I have to retrieve them from a list. This could be refactored.
else:
    f = open(jsonfile, 'r')
    data = json.load(f)
    f.close()
    print("------------------------------------")
    print("Your Daily Log")
    print("------------------------------------")
    k = 1
    for i in data['projects']:
        print_graph(k, i['title'], i['count'])
        k = k+1

# Some example json
# {
# "projects": [
# { "title":"JoS Review" , "count":14 },
# { "title":"Mayan semantics review article" , "count":40 },
# { "title":"Swarms" , "count":3 }
# ]
# }