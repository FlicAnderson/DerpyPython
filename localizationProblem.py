# Lost in Localization problem 1785 @ http://acm.timus.ru/problem.aspx?num=1785

# import library
import sys
# write input from commandline argument to variable
num_monsters = int(sys.argv[1])

# print num_monsters if there are 0
#if num_monsters <= 0:
#    print "Everything is fine - " + str(num_monsters) + " monsters"

if num_monsters >= 1 and num_monsters <= 4:
    monster_vol = "a few"
    print "You have " + monster_vol + " monsters"
elif num_monsters >= 5 and num_monsters <= 9:
    monster_vol = "several"
    print "You have " + monster_vol + " monsters"
elif num_monsters >= 10 and num_monsters <= 19:
    monster_vol = "a pack of"
    print "You have " + monster_vol + " monsters"
elif num_monsters >= 20 and num_monsters <= 49:
    monster_vol = "lots of"
    print "You have " + monster_vol + " monsters"
elif num_monsters >= 50 and num_monsters <= 99:
    monster_vol = "a horde of"
    print "You have " + monster_vol + " monsters"
elif num_monsters >= 100 and num_monsters <= 249:
    monster_vol = "a throng of"
    print "You have " + monster_vol + " monsters"
elif num_monsters >= 250 and num_monsters <= 499:
    monster_vol = "a swarm of"
    print "You have " + monster_vol + " monsters"
elif num_monsters >= 500 and num_monsters <= 999:
    monster_vol = "zounds of"
    print "You have " + monster_vol + " monsters"
else:
    monster_vol = "a legion of"
    print "You have " + monster_vol + " monsters"