# -*- coding: utf-8 -*-
import sys
import urllib2
import codecs

class Beautifier:
    def __init__(self):
        pass

    def apply(self, content, phonetic):
        content = self.eol_with_brackets(content)
        parts = content.split('\\n')
        outs = []
        for part in parts:
            #print '[' + part + ']'
            out = self.replace_phonetic(part, phonetic)
            out = self.color_type(out)
            outs.append(out)        
        return '<br/>'.join(outs)

    def eol_with_brackets(self, content):
        return content.replace('(\\n', '(')
    
    def color_type(self, line):
        if line[0:2] == '<<' and line[-2:] == '>>':
            return '<font color="red">' + line + '</font>'
        else:
            return line

    def replace_phonetic(self, line, phonetic):
        if line[0] == '[' and line[-1] == ']':
            return phonetic
        else:
            return line

class PhoneticHelper:
    def __init__(self, w):
        self.word = w
        self.phonetic = ''

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
            self.phonetic = ''

    def __repr__(self):
        return self.word + '\t' + self.phonetic

class Entry:
    def __init__(self, w):
        self.word = w
        self.content = ''

    def set_content(self, content):
        #if self.phonetic:
        #    parts = content.split('\\n')
        #    p = parts[1].strip()
        #    if p[0] == '[' and p[-1] == ']':
        #        parts[1] = self.phonetic
        #    self.content = '<br/>'.join(parts)
        #else:
        self.content = content

    def __repr__(self):
        return self.word + '\n' + self.content

class Dictionary:
    def __init__(self, filename):
        self.entries = {}
        dict_f = file(filename, 'r')
        i = 0
        for line in dict_f:
            i = i + 1
            line = line.replace('\n', '')
            parts = line.split('\t')
            word = parts[0]
            entry = Entry(word)
            if len(parts) > 1:
                entry.set_content(parts[1])
            self.entries[word] = entry

        dict_f.close()
        print 'Load %d entries from %s' % (len(self.entries), filename)

    def get_entry(self, word):
        if word in self.entries:
            return self.entries[word]
        else:
            return None

def main():
    dicPhonetic = Dictionary('phonetic.txt')
    apple = dicPhonetic.get_entry('apple')
    phonetic = apple.content

    b = Beautifier()
    dic21 = Dictionary('21shijishuangxiangcidian-big5.txt')
    apple = dic21.get_entry('apple')
    #apple.fetch_phonetic()
    print apple
    print b.apply(apple.content, phonetic)

def old_main():
    words = {}

    # Entrys
    words_f = file('7000_words.txt', 'r')
    for line in words_f:
        line = line.replace('\n', '').strip()
        word = Entry(line)
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
            word = Entry(key)
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
    out_f = codecs.open('21dic_7000.txt', 'w', 'utf-8')
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
        word = Entry(sys.argv[1])
        word.fetch_phonetic()
        print word  
