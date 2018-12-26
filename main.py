#Reddit Web Bot.
import praw
reddit = praw.Reddit('bot1')
subreddit = reddit.subreddit("dankmemes")

def explore():
    for submission in subreddit.hot(limit=5):
        print("Title:", submission.title)
        print("Score:", submission.ups)
        print("Url:", submission.url)
        print("Visited:", submission.visited)
        print("Media:", submission.secure_media)
        print("---------------------------------\n")
explore()