#!/usr/bin/env python
import thread
import commands
import getopt, sys
import os
import subprocess
import random
from time import localtime, strftime, sleep
import socket
import urllib2

def get_phonetic(word):
    print word

    # Get phonetic from cdict.net
    response = urllib2.urlopen("http://cdict.net/?q=%s" % word.replace(" ", "+"))
    html = response.read()
    start = html.find("<span class=trans>", 0)
    if start >= 0:
        end = html.find("</span>", start)
    else:
        start = 0
        end = 0
    phonetic = html[start + 18 :end]
    phonetic = phonetic.replace("<font face=courier>", "")
    phonetic = phonetic.replace("</font>", "").strip()

    return phonetic


def main(word):
    phonetic = get_phonetic(word)
    print phonetic

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print 'Usage: ' + sys.argv[0] + ' <WORD>'
    else:
        main(sys.argv[1])

