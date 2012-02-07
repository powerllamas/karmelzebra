# -*- coding: utf-8 -*-
import csv
import json

from collections import defaultdict

config = {'infile': 'comments.json', 'outfile': 'reddits.csv'}

def app():
    strengths = defaultdict(int)
    reddits = set()
    comments = None
    print "Loading: {0}".format(config['infile'])
    with open(config['infile']) as infile:
        comments = json.load(infile)

    for comment in comments.itervalues():
        reddit_name = comment[2]
        reddits.add(reddit_name)
        strengths[reddit_name] += 1

    print "Writing: {0}".format(config['outfile'])
    with open(config['outfile'], 'w') as outfile:
        writer = csv.writer(outfile)
        for number, reddit_name in enumerate(sorted(reddits), start=1):
            strength = strengths[reddit_name]
            writer.writerow([number, reddit_name, strength])
    print "Done!"


if __name__ == '__main__':
    try:
        app()
    except KeyboardInterrupt:
        print "\nNumbering reddits and finding their strengths stopped by user. Bye!"
