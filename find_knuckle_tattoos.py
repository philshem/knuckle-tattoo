#!/usr/bin/python3

"""
find_knuckle_tattoos.py

This code reads an input file which is a newline separated list of words.
It then finds all words of length N and 2*N (generally, N=4).
It then rearranges the words of length N, and sees if the new words are found in the list of words of length N and N*2.
The rearrangement is similar to if you had two words tattooed on your knuckles, and then intertwined your fingers.
e.g. ABCD and 1234 would becomes A1C3 and B2D4. Of course, these are not valid words.
It prints, in tsv format (tab-csv), the initial words, the final words, and the word type (2 words of length N, or 1 word of length 2*N)
"""

import itertools
import sys

try:
  word_list_file = sys.argv[1]
except:
  print('requires one command line argument - a path to a word list file')
  exit(0)

with open(word_list_file,'r') as fp:
	words = fp.readlines()#read().split('\n')

# delimiter for printing the csv
DL = '\t'

# debugging, make a smaller wordlist
#words = words[0:100000]

# playing length 4 words
N = 4

# small (N, or 4) letter words, good for one hand
word_small = [x.strip().upper() for x in words if len(x.strip()) == N]
# big (2*N, or 8) letter words, good for two hands
word_big = [x.strip().upper() for x in words if len(x.strip()) == N * 2]

# all permutations
# including front/back and back/front
all_pairs_word_small = itertools.permutations(word_small,2)
all_pairs_word_small = list(all_pairs_word_small)
# debugging
#all_pairs_word4 = itertools.permutations(['ABCD','WXYZ', '1234'],2)

# but, we also need 2 word possible combinations, e.g. STAY TRUE, instead of only 8 letter words
word_2xsmall = [''.join(x) for x in all_pairs_word_small]

# sets and dicts are faster for lookups than arrays, so we convert arrays to sets
word_small = set(word_small)
word_big = set(word_big)
word_2xsmall = set(word_2xsmall)
all_pairs_word_small = set(all_pairs_word_small)

# show some stats
if True:
	print('count small words:',len(word_small))
	print('count big words:',len(word_big))
	print('count small word permutations:',len(all_pairs_word_small))
	#print('count big words from small words:', len(word_2xsmall)) # kind of obvious it's the same as above

# print csv header
print(DL.join(('left','right','together','type_of_word')))
        
# search all word space
for x in all_pairs_word_small:
	# left hand
	left = list(x[0])
	# right hand
	right = list(x[1])

	# mixed hands, split individual words into letters
	mix = ''
	for i in range(N):
		mix += left[i] + right[i]

	# debugging		
	#print(x,left,right, mix)

	# search full list of 8 and 2x4 letter words
	if mix in word_big:
		print(DL.join((x[0],x[1],mix,'1x big word')))
	elif mix in word_2xsmall:
		print(DL.join((x[0],x[1],mix,'2x small words')))

	#break
