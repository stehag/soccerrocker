import json

from func import getMatches


data = getMatches()

with open('matchesmerge.json', 'w') as outfile:
    json.dump(data, outfile)

