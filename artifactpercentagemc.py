import random


def round():
    deck = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,
            "T","a","a","a","b","b","b","c","c","c","d","d","d","e","e","e"]
    cardcount = 0
    hazardsdrawn = []
    hazards = ["a","b","c","d","e"]
    cavein = False
    treasuredrawn = False

    while not cavein:
        currentcard = random.choice(deck)
        cardcount+=1
        deck.remove(currentcard)
        if currentcard in hazards:
            if currentcard in hazardsdrawn:
                cavein = True
            else:
                hazardsdrawn.append(currentcard)
        elif currentcard == "T":
            treasuredrawn = True

    return [cardcount,treasuredrawn]


def montecarlo(roundcount):
    valuedict = {}
    for x in range (0,roundcount):
        count = round()
        if not count[0] in valuedict:
            valuedict[count[0]] = [1,0]
        else:
            valuedict[count[0]][0] += 1
        if count[1] == True:
            valuedict[count[0]][1]+=1

    for key in sorted(valuedict):
        print ("%s,%s" % (key, valuedict[key]))

    for key in sorted(valuedict):
        print ("%s,%s" % (key, valuedict[key][1]/valuedict[key][0]))


montecarlo(10000000)
