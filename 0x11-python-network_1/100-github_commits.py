#!/usr/bin/python3
"""
Please list 10 commits (from the most recent to oldest)
of the repository “rails” by the user “rails”
You must use the GitHub API, here is the documentation
https://developer.github.com/v3/repos/commits/
Print all commits by: `<sha>: <author name>` (one by line)
"""
from sys import argv
import requests


if __name__ == '__main__':
    # Check if two command-line arguments are provided
    if len(argv) != 3:
        print("Usage: python script_name.py repository_name owner_name")
        exit(1)

    # Make the API request
    url = 'https://api.github.com/repos/{}/{}/commits'.format(argv[2], argv[1])
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        commits = response.json()

        # Print the 10 most recent commits (or less if there are fewer)
        for commit in commits[:10]:
            sha = commit.get('sha')
            author_name = commit.get('commit').get('author').get('name')
            print(f"{sha}: {author_name}")
    else:
        print(f"Failed to fetch commits. Status code: {response.status_code}")
