#!/usr/bin/env python
import sys
playerNum = sys.argv[1]
print "I am player %s" % playerNum

def readOpponentTurn():
    opp1 = raw_input()
    opp2 = raw_input()
    opp3 = raw_input()

def double(slot):
    print "1"
    print "dbl"
    print slot

def zero(slot):
    print "2"
    print slot
    print zero

def succ(slot):
    print "1"
    print "succ"
    print slot

def dec(slot):
    print "1"
    print "dec"
    print slot

if(playerNum == 1):
    readOpponentTurn()

turnNum = 0
while(1 == 1):
    turnNum = turnNum + 1
    if(turnNum == 0):
        zero(0)
    elif(turnNum == 1):
        succ(0)
    elif(turnNum <= 6):
        dbl(0)
    elif(turnNum >= 7):
        dec(0)
        turnNum = 0
