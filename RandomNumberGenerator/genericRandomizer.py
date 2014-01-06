"""
How it works:
1. Grab a random wikipedia article
2. Take a sequence of html characters of length num
3. Get their numerical values

Credits: http://codegolf.stackexchange.com/a/16399
"""

import urllib2
from random import randint
def getRandom(num):
    response = urllib2.urlopen('http://en.wikipedia.org/wiki/Special:Random')
    html = response.read()
    html = html.replace(" ", "")
    htmllen = len(html)

    l =  randint(0, htmllen - num)
    data = html[l:l+num]
    return [ ord(x) for x in list(data) ]

print getRandom(25)