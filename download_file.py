#!/usr/bin/env python
import requests

def download(url):
    get_response = requests.get(url)
    filename = url.split("/")[-1]
    print(filename)
    with open(filename, "wb") as out_file:
        out_file.write(get_response.content)

download("https://miro.medium.com/max/700/0*scVRuv7_0HZ65Yup.jpg")