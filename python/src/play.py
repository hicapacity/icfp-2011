#!/usr/bin/env python
import sys
playerNum = sys.argv[1]
#print "I am player %s" % playerNum

def readOpponentTurn():
    opp1 = raw_input()
    opp2 = raw_input()
    opp3 = raw_input()

def dbl(slot):
    print "1"
    print "dbl"
    print slot

def zero(slot):
    #print >> sys.stderr, "zero!"
    print "2"
    print slot
    print "zero"

def succ(slot):
    print "1"
    print "succ"
    print slot

def dec(slot):
    print "1"
    print "dec"
    print slot

def simpleAttack(slot):
    zero(slot)
    succ(slot)
    dbl(slot)
    dbl(slot)
    dbl(slot)
    dbl(slot)
    dbl(slot)
    dec(slot)

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
