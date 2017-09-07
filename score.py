import random

def score():
    if random_num >=90:
        print "Score: "+ str(random_num) + " Your grade is A "
    elif random_num >=80:
        print "Score: "+ str(random_num)+ " Your grade is B "
    elif random_num >=70:
        print "Score: "+ str(random_num) + " Your grade is C "
    else:
        print "Score: "+ str(random_num) + " Your grade is D "

print "Scores and Grades "
count=1;
while count < 11:
    random_num = random.random()
    random_num = random.randint(60,101)
    score()
    count=count+1




