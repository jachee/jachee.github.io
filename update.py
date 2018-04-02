#! /bin/env python

import requests, markdown

r = requests.get("https://jachee.github.io/toread.md")
html = markdown.markdown(r.text)
print(html)
