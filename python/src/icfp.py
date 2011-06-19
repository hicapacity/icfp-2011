def readOpponentTurn():
    opp1 = raw_input()
    opp2 = raw_input()
    opp3 = raw_input()

def dbl1(slot):
    print "1"
    print "dbl"
    print slot

def dbl(slot):
    print "1"
    print "dbl"
    print slot

def zero2(slot):
    #print >> sys.stderr, "zero!"
    print "2"
    print slot
    print "zero"

def zero(slot):
    #print >> sys.stderr, "zero!"
    print "2"
    print slot
    print "zero"

def succ(slot):
    print "1"
    print "succ"
    print slot

def succ1(slot):
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

def large(slot):
    zero(slot)
    succ(slot)
    dbl(slot)
    dbl(slot)
    dbl(slot)
    dbl(slot)
    dbl(slot)
    dbl(slot)
    dbl(slot)
    dbl(slot)
    dbl(slot)
    dbl(slot)
    dbl(slot)
    dbl(slot)
    dbl(slot)
    dbl(slot)

def s2(slot):
    print "2"
    print slot
    print "S"

def s1(slot):
    print "1"
    print "S"
    print slot

def i1(slot):
    print "1"
    print "I"
    print slot

def i2(slot):
    print "2"
    print slot
    print "I"

def k1(slot):
    print "1"
    print "K"
    print slot

def k2(slot):
    print "2"
    print slot
    print "K"

# Get the value num into slot slot
def buildNum(slot, num):
    if(num == 0):
        zero2(slot)
        return

    if(num == 1):
        zero2(slot)
        succ1(slot)
        return

    if((num % 2) == 0):
        buildNum(slot, num/2)
        dbl1(slot)
    else:
        buildNum(slot, num/2)
        dbl1(slot)
        succ1(slot)


def build(num):
    if(num == 0):
        print "0"
        return

    if(num == 1):
        print "0"
        print "1"
        return

    if((num % 2) == 0):
        build(num/2)
        print num
    else:
        build(num/2)
        print num - 1
        print num


#def notes():
#    5 = 0 1 2 4 5
#    5 = zero succ dbl dbl succ
#    7 = 0 1 2 4 5 6 7
#    7 = 0 1 2 3 6 7
#    8 = 0 1 2 4 8
#    9 = 0 1 2 4 9
#    10 = 0 1 2 4 8 9 10
#    10 = 0 1 2 3 6 8 9 10
#    10 = 0 1 2 4 5 10
#    10 = build(5) build(2) build(1)
#    12 = 0 1 2 4 8 9 10 11 12
#    12 = 0 1 2 3 6 12
#    # devide by 2, round down (build that num) count up
#    13 = 0 1 2 4 8 9 10 11 12 13
#    13 = 0 1 2 3 6 12 13
#    13 = build(6) build(3) build(1)
#    14 = 0 1 2 3 6 12 13 14
#    14 = 0 1 2 3 6 7 14
#    14 = build(7) build(3) build(1)
#    16 = 0 1 2 4 8 16
#    16 = build(8) build(4) build(2) build(1)
#    21 = 0 1 2 4 5 10 20 21
