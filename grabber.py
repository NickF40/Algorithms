import praw
from configs import *

reddit = praw.Reddit(client_id=client['id'], client_secret=client['secret'], username=client['username'], password=client['password'], user_agent=client['agent'])

subbr = reddit.subreddit('memes')

hot = subbr.hot(limit=10) 
print("\n".join([str(sub.__dict__) for sub in hot]))

# print('\n'.join([sub.title for sub in  subbr.hot(limit=2)]))


