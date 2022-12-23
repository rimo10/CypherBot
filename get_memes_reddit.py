import random

import praw
import datetime


def getMeme():
    reddit = praw.Reddit(
        client_id='9d0Luruhk-AS1Fzdsy6-jA',
        client_secret='NVan9cCf-xdd6yLpKqiu7i3TJauJpQ',
        user_agent='rimoghosh',
    )
    image_urls = []
    image_titles = []
    subs = ['dankmemes', 'memes', 'holup']
    for sub in subs:
        subreddit = reddit.subreddit(sub)
        posts = subreddit.hot(limit=10)

        for post in posts:
            if post.url.endswith(('.jpg', '.png', '.jpeg')):
                image_urls.append(post.url)
            image_titles.append(post.title)

    return random.choice(image_urls)
    # print(image_urls)


if __name__ == "__main__":
    print(getMeme())
