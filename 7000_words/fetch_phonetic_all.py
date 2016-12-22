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

head = ""
tail = ""
level = 0

def filename(word):
	word = word.replace("'", "_")
	word = word.replace(" ", "_")
	return word

def add_word(word, textf):
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

	textf.write("%s\t%s\n" % (word, phonetic))
	textf.flush()


def main():
	f = open("7000.txt", "r")
	textf = open("phonetic.txt", "w")

	for line in f:
		line = line[:-1]
		words = line.split('/')
		for word in words:
			word = word.replace("(1)", "")
			word = word.replace("(2)", "")
			word = word.replace("(3)", "")
			word = word.strip()
			if len(word) == 0:
				continue
			if len(word) > 5 and word[0:5] == "LEVEL":
				if word[6:7] != '1':
					pass
				print word
			else:
				n = word.find('(')
				m = word.find(')')
				if n == -1:
					add_word(word.strip(), textf)
				else:
					opt = word[n+1:m]
					sword = word.replace("("+opt+")", "")
					add_word(sword.strip(), textf)
					cword = word.replace("(", "")
					cword = cword.replace(")", "")
					add_word(cword.strip(), textf)

				t = 10 * random.random()
				print t
				sleep(t)


	f.close()
	textf.close()
	

if __name__ == "__main__":
	main()

