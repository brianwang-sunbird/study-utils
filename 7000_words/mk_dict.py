# -*- coding: utf-8 -*-
import sys
import urllib2
import codecs

class Word:

	def __init__(self, w):
		self.word = w
		self.phonetic = False
		self.content = ''

	def set_phonetic(self, phonetic):
		self.phonetic = phonetic

	def set_content(self, content):
		if self.phonetic:
			parts = content.split('\\n')
			parts[1] = self.phonetic
			self.content = '<br/>'.join(parts)
		else:
			self.content = content

	def fetch_phonetic(self):
		# Get phonetic from cdict.net
		response = urllib2.urlopen("http://cdict.net/?q=%s" % self.word.replace(" ", "+"))
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

		if len(phonetic) != 0:
			self.phonetic = phonetic
		else:
			self.phonetic = False

	def __repr__(self):
		if self.phonetic:
			return self.word + '\t' + self.phonetic
		else:
			return self.word

	def to_dict(self):
		return self.word + '\t' + self.content

def main():
	words = {}

	# Words
	words_f = file('7000_words.txt', 'r')
	for line in words_f:
		line = line.replace('\n', '').strip()
		word = Word(line)
		words[line] = word

	words_f.close()
	#print words

	# Phonetic
	phonetic_f = file('phonetic.txt', 'r')
	for line in phonetic_f:
		line = line.replace('\n', '')
		parts = line.split('\t')
		key = parts[0].strip()
		if key in words:
			word = words[key]
		else:
			word = Word(key)
			words[key] = word

		if len(parts) > 1:
			phonetic = parts[1].strip()
			if len(phonetic) != 0:
				word.set_phonetic(phonetic)

	phonetic_f.close()

	# Following will fetch phonetic from cdict.net 
	# and append the new phonetic in the end of phonetic.txt
	# May has issues
	'''
	phonetic_f = codecs.open('phonetic.txt', 'a+', 'utf-8')
	for key in words:
		word = words[key]
		if word.phonetic == False:
			word.fetch_phonetic()
			if word.phonetic:
				print word
				phonetic_f.write(unicode(str(word), 'big5') + '\n')
	phonetic_f.close()
	'''
	# Dict
	dict_f = file('21shijishuangxiangcidian-big5.txt', 'r')
	out_f = codecs.open('output.txt', 'w', 'utf-8')
	i = 0
	for line in dict_f:
		i = i + 1
		line = line.replace('\n', '')
		parts = line.split('\t')
		key = parts[0]
		if key in words:
			word = words[key]
			word.set_content(parts[1])
			out_f.write(unicode(str(word.to_dict()), 'utf-8') + '\n')

	dict_f.close()
	out_f.close()

if __name__ == '__main__':
	if len(sys.argv) == 1:
		main()
	else:
		word = Word(sys.argv[1])
		word.fetch_phonetic()
		print word	
