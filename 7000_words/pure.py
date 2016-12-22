#!/usr/bin/env python


def main():
	f = open("7000.txt", "r")


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
				#print word
			else:
				n = word.find('(')
				m = word.find(')')
				if n == -1:
					print word.strip()
					#add_word(word.strip(), textf)
				else:
					opt = word[n+1:m]
					sword = word.replace("("+opt+")", "")
					#add_word(sword.strip(), textf)
					print sword.strip()
					cword = word.replace("(", "")
					cword = cword.replace(")", "")
					cword = cword.replace(" ", "", 10)
					#add_word(cword.strip(), textf)
					print cword.strip()

				#t = 10 * random.random()
				#print t
				#sleep(t)


	f.close()

	

if __name__ == "__main__":
	main()

