#!/usr/bin/python3

import requests
import csv

def fetch_and_print_posts():
    request = requests.get("https://jsonplaceholder.typicode.com/posts")
    request_json = request.json()
    print("Status Code: {}".format(request.status_code))

    if request.status_code == 200:
        for _ in request_json:
            print(_["title"])

def fetch_and_save_posts():

    request = requests.get("https://jsonplaceholder.typicode.com/posts")
    request_json = request.json()
    print("Status Code: {}".format(request.status_code))

    posts = []
    if request.status_code == 200:
        for _ in request_json:
            posts.append({"id": _["id"], "title": _["title"], "body": _["body"]})

    with open("posts.csv", 'w', encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["id", "title", "body"])
        writer.writeheader()
        writer.writerows(posts)
