#!/usr/bin/python3
"""
Reddit API - Word counting
"""
import requests


def count_words(subreddit, word_list, word_count={}, after=None):
    """
    Queries the Reddit API, parses the title of all hot articles, and prints
    a sorted count of given keywords.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
    params = {'limit': 100}
    
    if after:
        params['after'] = after
    
    if not word_count:
        word_count = {word.lower(): 0 for word in word_list}
    
    try:
        response = requests.get(url, headers=headers, params=params, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            posts = data['data']['children']
            after = data['data']['after']
            
            for post in posts:
                title = post['data']['title'].lower()
                for word in word_list:
                    word_lower = word.lower()
                    word_count[word_lower] += title.split().count(word_lower)
            
            if after:
                return count_words(subreddit, word_list, word_count, after)
            else:
                sorted_words = sorted(word_count.items(), key=lambda x: (-x[1], x[0]))
                for word, count in sorted_words:
                    if count > 0:
                        print(f"{word}: {count}")
                return word_count
        else:
            return None
    except Exception:
        return None


if __name__ == "__main__":
    import sys
    if len(sys.argv) < 3:
        print("Usage: ./3-count.py <subreddit> <list of keywords>")
    else:
        subreddit = sys.argv[1]
        word_list = [word for word in sys.argv[2].split()]
        count_words(subreddit, word_list)
