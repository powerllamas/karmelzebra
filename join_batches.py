# -*- coding: utf-8 -*-
import os
import sys
import json


batch_folder = 'dump_copy'
config = {'batch_folder': 'dump', 'output_filename': 'comments.json'}

def app():
    comments = {}
    for filename in os.listdir(config['batch_folder']):
        if not filename.endswith('.json'):
            continue
        print "Merging: {0}".format(filename)
        with open(os.path.join(config['batch_folder'], filename)) as f:
            data = json.load(f)
            for comment_id in data.iterkeys():
                comments[comment_id] = data[comment_id]
    print "Writing: {0}".format(config['output_filename'])
    sys.stdout.flush()
    comments_json = json.dumps(comments, sort_keys=True)
    with open(config['output_filename'], 'w') as f:
        f.write(comments_json)
    print "Done!"


if __name__ == '__main__':
    try:
        app()
    except KeyboardInterrupt:
        print "\nJoining batches stopped by user. Bye!"
