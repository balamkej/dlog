#!/usr/bin/env python3

import argparse, json

try:
    with open('dlog.json') as file:
        pass
except IOError as e:
    print("Unable to open file")



# Some example json
# {
# "projects": [
# { "title":"JoS Review" , "count":"14" , "init_date":"2/15" }, 
# { "title":"Mayan semantics review article" , "count":"40" , "init_date":"3/15" }, 
# { "title":"Swarms" , "count":"3" , "init_date":"2/15" }
# ]
# }