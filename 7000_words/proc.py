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
folder = "l1"

def filename(word):
	word = word.replace("'", "_")
	word = word.replace(" ", "_")
	return word

def translate(word):
	#put_head(word)
	cmd = "./SDCV.sh \"" + word + "\" ./output/" + folder + "/" + filename(word) + ".html"
	print cmd
	commands.getstatusoutput(cmd)
	#put_tail(word)

def load_template():
	global head, tail
	th = open("template.head", "r")
	tl = open("template.tail", "r")
	for line in th:
		head = head + line
	for line in tl:
		tail = tail + line
	th.close()
	tl.close()

def put_head(word):
	f = open("./output/" + folder + "/" + filename(word) + ".html", "w")
	f.write(head)
	f.close()

def put_tail(word):
    f = open("./output/" + folder + "/" + filename(word) + ".html", "a")
    f.write(tail)
    f.close()

def add_word(f, word, textf):
	print word
	f.write("<a href=\"" + folder + "/" + filename(word) + ".html\">" + word + "</a>\n")

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
	phonetic = phonetic.replace("</font>", "")

	textf.write("%s\t%s\n" % (word, phonetic))
	textf.flush()
	#textf.write(word + "\n");

	#translate(word)

def main():
	global folder
	load_template()
	f = open("7000.txt", "r")
	textf = open("words.txt", "w")

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
					levelf.write(tail)
					levelf.close()
				folder = "l%s" % word[6:7]
				levelf = open("./output/7000_words_" + filename(word[0:7]) + ".html", "w")
				levelf.write(head)
				levelf.write("<h1>"+word+"</h1>\n");
				print word
			else:
				n = word.find('(')
				m = word.find(')')
				if n == -1:
					add_word(levelf, word.strip(), textf)
				else:
					opt = word[n+1:m]
					sword = word.replace("("+opt+")", "")
					add_word(levelf, sword.strip(), textf)
					cword = word.replace("(", "")
					cword = cword.replace(")", "")
					add_word(levelf, cword.strip(), textf)

				t = 10 * random.random()
				print t
				sleep(t)


	f.close()
	levelf.close()
	textf.close()
	

if __name__ == "__main__":
	main()

