# -*- coding: utf-8 -*-
import json
import csv
import itertools

from collections import defaultdict


config = {'infile': 'user_to_reddit.json', 'outfile': 'reddits_connections.csv'}

def app():
    users = None
    print "Loading: {0}".format(config['infile'])
    with open(config['infile']) as infile:
        users = json.load(infile)

    connections = defaultdict(int)
    for reddits in users.itervalues():
        reddits_list = sorted(reddits.keys())
        for combination in itertools.combinations(reddits_list, 2):
            connections[combination] += 1

    print "Writing: {0}".format(config['outfile'])
    with open(config['outfile'], 'w') as outfile:
        writer = csv.writer(outfile)
        for reddits, strength in sorted(connections.iteritems()):
            reddit1, reddit2 = reddits
            writer.writerow([reddit1, reddit2, strength])
    print "Done!"


if __name__ == '__main__':
    try:
        app()
    except KeyboardInterrupt:
        print "\nFinding reddits connections stopped by user. Bye!"
