# -*- coding: utf-8 -*-
import json
import csv


config = {'infile': 'comments.json', 'outfile': 'comments.csv'}

def app():
    comments = None
    print "Loading: {0}".format(config['infile'])
    with open(config['infile']) as infile:
        comments = json.load(infile)
    print "Writing: {0}".format(config['outfile'])
    with open(config['outfile'], 'w') as outfile:
        writer = csv.writer(outfile)
        for comment_id in sorted(comments.iterkeys()):
            writer.writerow(comments[comment_id])
    print "Done!"


if __name__ == '__main__':
    try:
        app()
    except KeyboardInterrupt:
        print "\nConversion to csv stopped by user. Bye!"
