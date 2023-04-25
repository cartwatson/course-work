#!/usr/bin/python3

import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin
import sys


def crawl(url, maxDepth, depth, visited):
    # Check the current depth of recursion; return now if you have gone too deep
    if depth > maxDepth:
        return

    # Print this URL with indentation indicating the current depth of recursion
    print("    " * depth, end="")
    # print current link
    print(url)
    visited.add(url)

    try:
        response = requests.get(url)
        if not response.ok:
            print(f"crawl({url}): {response.status_code} {response.reason}")
            return

        html = BeautifulSoup(response.text, 'html.parser')
        links = html.find_all('a')
        for a in links:
            link = a.get('href')
            if link:
                # Create an absolute address from a (possibly) relative URL
                absoluteURL = urljoin(url, link)

                # Only deal with resources accessible over HTTP or HTTPS
                if absoluteURL.startswith('http'):
                    # Trim fragments ('#' to the end) from URLs
                    if '#' in absoluteURL:
                        temp = absoluteURL.split("#", 1)
                        absoluteURL = temp[0]
                    if absoluteURL not in visited:
                        # call crawl() on unvisited URLs
                        crawl(absoluteURL, maxDepth, depth + 1, visited)
                        # set data structure to keep track of URLs you've already visited
                        visited.add(absoluteURL)

    except Exception as e:
        print(f"crawl(): {e}")
    return


def main():
    # An absolute URL is required to begin
    if len(sys.argv) < 2:
        print("Error: no absolute URL supplied")
        sys.exit(1)
    else:
        url = sys.argv[1]

    # determine whether variable `url` contains an absolute URL
    if not url.startswith('http'):
        print("Error: supplied URL is not absolute")
        sys.exit(1)

    # allow the user to optionally override the default recursion depth of 3
    if len(sys.argv) < 3:
        maxDepth = 3
    else:
        maxDepth = int(sys.argv[2])

    # init list of visited sites and level depth
    visited = set()
    # visited.add(url)
    depth = 0

    # determines plural for string below
    plural = 's'
    if maxDepth == 1:
        plural = ''
    print(f"Crawling from {url} to a maximum depth of {maxDepth} link{plural}")

    # crawl() keeps track of the max depth itself: no globals
    # print(url)
    crawl(url, maxDepth, depth, visited)


main()