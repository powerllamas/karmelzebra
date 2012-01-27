# -*- coding: utf-8 -*-
import json

from collections import defaultdict


config = {'infile': 'comments.json', 'users_file': 'user_to_reddit.json', 'reddits_file': 'reddit_to_user.json'}

def app():
    comments = None
    print "Loading: {0}".format(config['infile'])
    with open(config['infile']) as infile:
        comments = json.load(infile)

    users = defaultdict(lambda: defaultdict(int))
    reddits = defaultdict(lambda: defaultdict(int))
    for comment_id in comments.iterkeys():
        comment = comments[comment_id]
        username = comment[1]
        subreddit = comment[2]
        users[username][subreddit] += 1
        reddits[subreddit][username] += 1
    print "Writing: {0}".format(config['users_file'])
    with open(config['users_file'], 'w') as outfile:
        data = json.dumps(users, sort_keys=True, indent=2)
        outfile.write(data)
    print "Writing: {0}".format(config['reddits_file'])
    with open(config['reddits_file'], 'w') as outfile:
        data = json.dumps(reddits, sort_keys=True, indent=2)
        outfile.write(data)
    print "Done!"


if __name__ == '__main__':
    try:
        app()
    except KeyboardInterrupt:
        print "\nJoining batches stopped by user. Bye!"
