# coding: utf8
from glob import glob
import operator

def clean_str(s):
	rm = [',', '.', ';', '?', '!', '%', '*', '(', ')', 
		'=', '@', '#', '$', '+', '-', '<', '>']
	for ch in rm:
		s = s.replace(ch, '')
	return s

files = glob('*.srt')
words_dic = {}
ignore_words = set(['–'])

for file in files:
	fl = open(file).readlines()
	words_dic[file] = {}

	for line in fl:
		line = line.strip().lower()

		if line == '' or '-->' in line or line.isdigit():
			continue

		line = clean_str(line)
		words = line.split()
		words = [w for w in words if not (w.isdigit() or w in ignore_words)]

		for w in words:
			words_dic[file][w] = words_dic[file].get(w, 0) + 1

all_words = {}
for fl, dic in words_dic.items():
	print('{}\nTotal unique words: {}'.format(fl, len(dic)))
	for w, cnt in dic.items():
		all_words[w] = all_words.get(w, 0) + cnt

n_unique_words = len(all_words)
total_words = sum(all_words.values())
print('\n--All files together--')
print('Total unique words: {}'.format(n_unique_words))
print('Total words: {}'.format(total_words))

all_words = sorted(all_words.items(), key=operator.itemgetter(1),reverse=True)
p_acum = 0
i = 0
for w, cnt in all_words[:100]:
	p = 100.0 * cnt/total_words
	p_acum+= p
	print('{}\t{}\t{}\t{:.1f}%\t{:.1f}%'.format(i, w, cnt, p, p_acum))
	i+= 1
