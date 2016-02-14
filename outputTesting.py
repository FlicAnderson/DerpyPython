# write a program that creates a sentence containing various words,
# of which 3 words input from the commandline

import sys
thing1 = sys.argv[1]
thing2 = sys.argv[2]
thing3 = sys.argv[3]

print "Some text which is a story about " + thing1 + " but also contains vital information about " + thing2 + " but eventually ends with " + thing3 + "."

# to run this, would open commandline
# then navigate to the folder holding this script
# then run the following:

# $ python outputTesting.py frog weasel triumph
    # where python runs the interpreter on the script
    # outputTesting.py (script) represents sys.argv[0] - the FIRST argument
    # and frog, weasel and triumph are sys.argv 1-3.
    # NB: the sys.argv arguments 1:3 DO NOT need quotes to show string type
    # just as sys.argv 0 doesn't need them either