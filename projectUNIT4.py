import random

Trials = 0

headsnum = 0
tailsnum = 0

while(Trials < 10000):
    Coinflipson = [1,2]
    Heads = 1
    Tails = 2
    PersonFlips = random.choice(Coinflipson)
    if PersonFlips ==  Heads:
        headsnum = headsnum + 1
    else:
        tailsnum = tailsnum + 1   

    Trials += 1

headsper = (headsnum/Trials)
tailsper = (tailsnum/Trials)







print ("Total Trials:", Trials)
print ("Total heads:", headsnum)
print ("Total tails:",(tailsnum))
print ("Your chances of flipping a head during the trials was:",headsper)
print ("Your chances of flipping a tail during the trials was:",tailsper)
