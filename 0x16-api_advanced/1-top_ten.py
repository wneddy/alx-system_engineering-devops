#!/usr/bin/python3
"""
function that queries the Reddit API and prints
the titles of the first 10 hot posts listed for a given subreddit.
"""
import requests

def top_ten(subreddit):
    """Fetches and prints the titles of the first 10 hot posts from a subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {'User-agent': 'Mozilla/5.0'}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)

        # Check if the subreddit exists by ensuring a 200 status code.
        if response.status_code == 200:
            data = response.json()
            posts = data.get('data', {}).get('children', [])

            # Print the titles of the first 10 hot posts
            for post in posts:
                print(post['data']['title'])
        else:
            print(None)
    except Exception as e:
        print(None)
