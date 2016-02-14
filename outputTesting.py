# write a program that creates a sentence containing various words,
# of which 3 words input from the commandline

import sys
thing1 = sys.argv[1]
thing2 = sys.argv[2]
thing3 = sys.argv[3]

print "Some text which is a story about " + thing1 + " but also contains vital information about " + thing2 + " but eventually ends with " + thing3 + "."