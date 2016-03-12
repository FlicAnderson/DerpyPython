# accept 5 words input from the commandline, sort them into alphabetical order

import sys
word1 = sys.argv[1]
word2 = sys.argv[2]
word3 = sys.argv[3]
word4 = sys.argv[4]
word5 = sys.argv[5]

word_list = [word1, word2, word3, word4, word5]

print sorted(word_list)