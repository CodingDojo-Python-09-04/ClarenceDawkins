#Clarence Dawkins

words = "It's thanksgiving day  It's my birth day, too! "
x=[2,54,-2,7,12,98]

#Print index
def index():
    index = words.find("day")
    print index;

#Replace

def replace():
    replace1 = words.replace("day","month",1);
    replace2 = words.replace("day","month",2);
    print replace1;
    print replace2;


index()
replace()

#Min and max
print x
print min(x)
print max(x)

#First and Last

x=["hello",2,54,-2,7,12,98,"world"]
i=0;
end=len(x)-1;
print x[i] + x[end];

#New List
x=[19,2,54,-2,7,12,98,32,10,-3,6]
x.sort();
print x;

split = len(x)/2;
x1=x[:split];
x2=x[split:]

print str(x1) + " First List";
print str(x2) + " Second List";
x2.insert(0,x1)
print x2;



    




