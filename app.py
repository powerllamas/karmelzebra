# -*- coding: utf-8 -*-
from collections import defaultdict

import json
import time

import reddit

config = {'sleep_time': 30, 'limit': 500}

file_template = 'dump/{0}_{1}.json'
file_numbering = 0

def save_as_json(dic, name, number):
    filename = file_template.format(name, number)
    data = json.dumps(dic, sort_keys=True, indent=2)
    with open(filename, 'w') as f:
        f.write(data)

def app():
    global file_numbering
    r = reddit.Reddit(user_agent='karmelzebra')

    while file_numbering < 500:
        print "Requesting batch nr {0}".format(file_numbering)
        try:
            names = defaultdict(list)
            reddits = defaultdict(list)
            comments = r.get_all_comments(limit=config['limit'], place_holder=None)

            comment_count = 0
            for comment in comments:
                names[str(comment.author)].append(str(comment.subreddit))
                reddits[str(comment.subreddit)].append(str(comment.author))
                comment_count += 1

            save_as_json(names, 'names', file_numbering)
            save_as_json(reddits, 'reddits', file_numbering)
            print "Batch nr {0} saved, {1} new records.".format(file_numbering, comment_count)
        except KeyboardInterrupt:
            raise
        except:
            print "Unexpected error"
            time.sleep(config['sleep_time'])
            continue
        finally:
            file_numbering += 1

        print "Sleeping now for {0} seconds...".format(config['sleep_time'])
        time.sleep(config['sleep_time'])

if __name__ == '__main__':
    try:
        app()
    except KeyboardInterrupt:
        print "\nDownloading stopped by user. Bye!"
