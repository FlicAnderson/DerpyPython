# accept arbitrary number of words input from the commandline, sort them into alphabetical order

import sys

word_list = sorted(sys.argv)
# print word_list[1:len(word_list)]
print word_list[1:]