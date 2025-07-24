# API Advanced

This directory contains advanced API interaction scripts for Reddit API.

## Files

- **0-subs.py**: Returns the number of subscribers for a given subreddit
- **1-top_ten.py**: Prints the titles of the top 10 hot posts for a given subreddit
- **2-recurse.py**: Recursively fetches all hot posts for a given subreddit
- **3-count.py**: Counts occurrences of specified keywords in post titles

## Usage

All scripts require a subreddit name as the first argument:

```bash
./0-subs.py programming
./1-top_ten.py python
./2-recurse.py learnpython
./3-count.py python "python code programming"
```

## Requirements

- Python 3
- requests library (install with `pip install requests`)
