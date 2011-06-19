#!/usr/bin/env python
import sys
from icfp import *
playerNum = sys.argv[1]
#print "I am player %s" % playerNum

if(playerNum == 1):
    readOpponentTurn()

turnNum = 0
realTurn = 0
while(1 == 1):
    turnNum = turnNum + 1
    realTurn = realTurn + 1
    simpleAttack(0)

    if(realTurn >= 10000000):
        sys.exit(0)
