#!/usr/bin/python3
"""
    script that takes in a URL, sends a request to the URL
    and displays the body of the response (decoded in utf-8).
"""


import sys
from urllib import request, error


if __name__ == "__main__":
    # Get the URL from the command line
    url = sys.argv[1]

    try:
        # Make a GET request to the URL
        with request.urlopen(url) as response:
            # Read and decode the response body
            print(response.read().decode('utf-8'))

    except error.HTTPError as e:
        # Handle HTTP errors and print the HTTP status code
        print("Error code: {}".format(e.code))
