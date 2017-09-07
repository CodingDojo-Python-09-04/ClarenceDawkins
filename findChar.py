

def findChar():
    char = raw_input("What character you want to find? ")
    for text in myList:
        if char in text:
            print(text)

myList =["Hello","World","my","name","is","Anna"]
findChar()

 
