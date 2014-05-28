#!/usr/bin/env python3

import argparse, json

try:
    with open('dlog.json') as file:
        pass
except IOError as e:
    print('Unable to find your Daily Log file. Use the --init flag to create a new one.')

parser = argparse.ArgumentParser(description='Daily Log App')

parser.add_argument('--init', action="store_true", dest='initialization_switch', default=False)
parser.add_argument('-a', action='append', dest='collection', help='Add n-many projects to your daily log. For example: -a book -a "book review" -a "journal article"')

results = parser.parse_args()

print('initialization_switch=', results.initialization_switch)
print('collection=', results.collection)

# Some example json
# {
# "projects": [
# { "title":"JoS Review" , "count":"14" , "init_date":"2/15" }, 
# { "title":"Mayan semantics review article" , "count":"40" , "init_date":"3/15" }, 
# { "title":"Swarms" , "count":"3" , "init_date":"2/15" }
# ]
# }