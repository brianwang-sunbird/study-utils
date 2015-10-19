#!/usr/bin/python
# -*- coding: utf8 -*-

import sys
import urllib2

encode = "utf8"
#if len(sys.argv) == 3:
#	encode = sys.argv[1]
word = sys.argv[1]

print "<html><head>\
<meta http-equiv=\"Content-Type\" content=\"text/html; charset=%s\">\
<meta http-equiv=\"expires\" content=\"0\">\
<meta http-equiv=\"Pragma\" content=\"no-cache\">\
<meta http-equiv=\"Cache-Control\" content=\"no-cache\"></head><body>" % encode

'''
# Get phonetic from cdict.net
response = urllib2.urlopen("http://cdict.net/?q=%s" % word.replace(" ", "+"))
html = response.read()
start = html.find("<span class=trans>", 0)
end = html.find("</span>", start)

print "<h2>%s %s</h2><br>" % (word, html[start:end])
'''
#f = open("./test.txt", "r")
input = sys.stdin.read()
for line in input.split("\n"):
	#print linea
	line = line.replace("  ", "&nbsp;&nbsp;")
	#line = line.replace("ɒ", "&#x254;")
	#line = line.replace("ŋ", "&#x14b;")
	#line = line.replace("ә:", "&#x25a;")
	print line + "<br>"

print "</body></html>"



