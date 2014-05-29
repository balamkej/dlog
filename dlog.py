#!/usr/bin/env python3

import argparse, json

try:
    with open('dlog.json') as file:
        pass
except IOError as e:
    print('Unable to find your Daily Log file. Use the --init flag to create a new one.')

parser = argparse.ArgumentParser(description='Daily Log App')

group = parser.add_mutually_exclusive_group()

group.add_argument('--init', action="store_true", dest='init_switch', default=False)
group.add_argument('-a', action='append', dest='collection', help='Add n-many projects to your daily log. For example: -a book -a "book review" -a "journal article"')
group.add_argument('-s', nargs=2, action='store', dest='swap', type=int, help='Takes two integer arguments, moving project i to location j.')

results = parser.parse_args()

print('init_switch=', results.init_switch)
print('collection=', results.collection)
print('swap=', results.swap)

# Some example json
# {
# "projects": [
# { "title":"JoS Review" , "count":"14" , "init_date":"2/15" }, 
# { "title":"Mayan semantics review article" , "count":"40" , "init_date":"3/15" }, 
# { "title":"Swarms" , "count":"3" , "init_date":"2/15" }
# ]
# }