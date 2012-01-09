# -*- coding: utf-8 -*-

import reddit

config = {'subreddits': ['politics', 'minecraft'], 'post_limit': 30}

def app():
    users = []
    r = reddit.Reddit(user_agent='karmelzebra')
    for subreddit_name in config['subreddits']:
        subreddit = r.get_subreddit(subreddit_name)
        submissions = subreddit.get_hot(limit=config['post_limit'])
        for sub in submissions:
            users.append(sub.author)

    for user in users:
        print user

if __name__ == '__main__':
    app()
