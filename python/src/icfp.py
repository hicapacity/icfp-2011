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

