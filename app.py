# -*- coding: utf-8 -*-
import sys
import json
import time

from collections import defaultdict

import reddit

config = {'sleep_time': 30, 'limit': 500}

file_template = 'dump/{0}_{1}.json'
file_numbering = 0

def save_as_json(dic, name, number):
    filename = file_template.format(name, number)
    data = json.dumps(dic, sort_keys=True)
    with open(filename, 'w') as f:
        f.write(data)

def app():
    global file_numbering
    r = reddit.Reddit(user_agent='karmelzebra')

    while file_numbering < 1000:
        print "Requesting batch nr {0}".format(file_numbering)
        try:
            batch = defaultdict(list)
            comments = r.get_all_comments(limit=config['limit'], place_holder=None)

            comment_count = 0
            for comment in comments:
                print '.',
                sys.stdout.flush()
                comment_id = comment.id
                author = str(comment.author)
                subreddit = str(comment.subreddit)
                batch[comment_id] = [comment_id, author, subreddit]
                comment_count += 1
            print

            save_as_json(batch, 'batch_26012012_0', file_numbering)
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
