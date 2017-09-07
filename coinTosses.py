import random

##def flip_coin(flip):
##    if flip == 0:
##        heads = heads + 1
##        print "Attempt #"+str(i)+": Throwing a coin... It's a head! ... Got " + str(heads) + " head(s) so far and " + str(tails) +" tail(s) so far "
##        i=i+1
##    else:
##        tails = tails +1
##        print "Attempt #"+str(i)+": Throwing a coin... It's a tail! ... Got " + str(heads) + " head(s) so far and " + str(tails) +" tail(s) so far "
##        i=i+1
##
##
##def winner():
##    if heads > tails:
##        print "heads wins! " + str(heads) + " Heads and "+ str(tails) +" Tails "
##    else:
##        print "tails wins! " + str(tails) + " Tails and "+ str(heads) +" Heads "
##    choice = raw_input("Are you ready to flip? Press y - yes or n - no : ")
    
print "Starting the program"

choice = raw_input("Are you ready to flip? Press y - yes or n - no : ")
choice = choice.upper()

while choice == "Y":
    heads = 0
    tails = 0
    i=1
    for flip in range(0,10):      
        flip = random.randint(0,1)
        if flip == 0:
            heads = heads + 1
            print "Attempt #"+str(i)+": Throwing a coin... It's a head! ... Got " + str(heads) + " head(s) so far and " + str(tails) +" tail(s) so far "
            i=i+1
        else:
            tails = tails +1
            print "Attempt #"+str(i)+": Throwing a coin... It's a tail! ... Got " + str(heads) + " head(s) so far and " + str(tails) +" tail(s) so far "
            i=i+1
    if heads > tails:
        print "heads wins! " + str(heads) + " Heads and "+ str(tails) +" Tails "
    else:
        print "tails wins! " + str(tails) + " Tails and "+ str(heads) +" Heads "
    choice = raw_input("Are you ready to flip? Press y - yes or n - no : ")
    choice = choice.upper()


    
