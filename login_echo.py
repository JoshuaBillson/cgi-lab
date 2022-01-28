#!/usr/bin/env python3

import os
import sys
import cgitb

from templates import echo_login_page


def print_post_data():
    posted_bytes = os.environ.get("CONTENT_LENGTH", 0)
    if posted_bytes:
        posted = sys.stdin.read(int(posted_bytes))
        print(f"<p> POSTED: <pre>")
        for line in posted.splitlines():
            print(line)
        print("</pre></p>")


def main():
    cgitb.enable()

    print("Content-Type: text/html\r\n")
    print(echo_login_page())
    print_post_data()


if __name__ == "__main__":
    main()
