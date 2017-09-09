
x = [4,"Tom",1,"Michael",5,7,"Jimmy Smith"]

def draw_star(x):
    end = len(x)
    for i in range(0,len(x)):
        num = x[i]       
        if type(x[i]) == int:            
            print "*"*num,
            print '\n'
        else:
            string= x[i]
            string = string.lower()
            start = 0
            end = len(string)-1
            while start <= end:
                print string[:1],                
                start = start + 1
            print '\n'

draw_star(x)
        
        
