# -*- coding: utf-8 -*-
import codecs

def main():
    words = {}
    fin = file('words.txt', 'r')
    fout = codecs.open('phonetic.tab', 'w', 'utf-8')

    for line in fin:
        if len(line) > 1:
            line = line[:-1]
        line = line.strip()
        parts = line.split('   ')
        word = parts[0]
        phonetic = line[len(word) + 1:].strip()
        words[word] = phonetic
    fin.close()

    for word in words:
        phonetic = words[word]
        s = ("%s\t%s\n" % (word, phonetic))
        fout.write(unicode(s, 'big5'))
    fout.close()

if __name__ == '__main__':
    main()
