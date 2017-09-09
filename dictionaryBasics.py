
students ={
    "name":"Anna",
    "age": "101",
    "country of birth": "The United States ",
    "favorite language": "Python "
    }

def print_dictionary(dic):
    for key, val in students.items():        
        print "My " + key + " is " + val

print_dictionary(students)
