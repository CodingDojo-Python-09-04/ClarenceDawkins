

###integer
##
def number():
    number = int(input("Please enter an integer: "))
    if number >= 100:
        print "That's a big number! "
    else:
        print "That's a small number "

number()
###String

def string():
    string = raw_input("Please enter a string ")
    numString = len(string)
    if numString >= 50:
        print "Long sentence. "
    else:
        print "Short sentence. "

string()

#List
def list():
    aL =[1,7,4,21]
    mL =[3,5,7,34,3,2,113,65,8,89]
    lL = [4,34,2,68,9,13,3,5,7,9,2,12,45,923]
    print str(aL) + " List 1 ";
    print str(mL) + " List 2 ";
    print str(lL)+ " List 3 ";
    if len(aL) >= 10:
        print "Big List! "
    else:
        print "Small List "

    if len(mL) >= 10:
        print "Big List! "
    else:
        print "Small List "

    if len(lL) >= 10:
        print "Big List! "
    else:
        print "Small List "

list()
    
