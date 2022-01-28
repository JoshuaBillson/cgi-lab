#!/usr/bin/env python3

import os
import json


def print_environment():
    print("Content-Type: text/plain\r\n")
    for k, v in os.environ.items():
        print(f"{k} = {v}")


def print_environment_json():
    print("Content-Type: application/json\r\n")
    print(json.dumps(dict(os.environ), indent=2))


def print_browser():
    browser = os.environ.get("HTTP_USER_AGENT")
    print("Content-Type: text/html\r\n")
    print(f"<p style='color:green;'>Your Browser Is: {browser}</p>")


def extract_query():
    query = dict()
    query_string = os.environ.get("QUERY_STRING")
    pairs = query_string.split("&")
    for pair in pairs:
        key, value = pair.split("=")
        query[key] = value
    return query


def main():
    print_environment()


if __name__ == "__main__":
    main()
