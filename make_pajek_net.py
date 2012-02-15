# -*- coding: utf-8 -*-
import csv

config = {'infile_connections': 'reddits_connections.csv', 'infile_reddits': 'reddits.csv',
        'outfile_net': 'reddit.reduced.net', 'outfile_vector': 'reddit.reduced.vec'}

def app():
    reddits = []
    reddits_map = {}
    connections = []
    print "Loading: {0}".format(config['infile_reddits'])
    with open(config['infile_reddits']) as infile:
        reader = csv.reader(infile)
        for row in reader:
            reddits_map[row[1]] = row[0]
            reddits.append(row)

    with open(config['infile_connections']) as infile:
        reader = csv.reader(infile)
        for row in reader:
            connections.append(row)

    print "Writing: {0}".format(config['outfile_net'])
    with open(config['outfile_net'], 'w') as outfile:
        outfile.write('*Vertices {0}\n'.format(len(reddits)))
        for reddit_idx, reddit_name, strength in reddits:
            outfile.write('{0} "{1}"\n'.format(reddit_idx, reddit_name))
        outfile.write('*Edges\n')
        for first, second, strength in connections:
            if not first in reddits_map:
                continue
            if not second in reddits_map:
                continue
            first_idx = reddits_map[first]
            second_idx = reddits_map[second]
            outfile.write('{0} {1} {2}\n'.format(first_idx, second_idx, strength))

    print "Writing: {0}".format(config['outfile_vector'])
    with open(config['outfile_vector'], 'w') as outfile:
        outfile.write('*Vertices {0}\n'.format(len(reddits)))
        for reddit_idx, reddit_name, strength in reddits:
            outfile.write('{0}\n'.format(strength))

    print "Done!"


if __name__ == '__main__':
    try:
        app()
    except KeyboardInterrupt:
        print "\nMaking Pajek net stopped by user. Bye!"
