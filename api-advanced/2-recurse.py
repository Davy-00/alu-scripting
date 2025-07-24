#!/usr/bin/python3
"""
Reddit API - Recursive API data fetching
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Queries the Reddit API and returns a list containing the titles of all
    hot articles for a given subreddit.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
    params = {'limit': 100}
    
    if after:
        params['after'] = after
    
    try:
        response = requests.get(url, headers=headers, params=params, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            posts = data['data']['children']
            after = data['data']['after']
            
            for post in posts:
                hot_list.append(post['data']['title'])
            
            if after:
                return recurse(subreddit, hot_list, after)
            else:
                return hot_list
        else:
            return None
    except Exception:
        return None


if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        result = recurse(sys.argv[1])
        if result:
            print(len(result))
        else:
            print(None)
