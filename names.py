
users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }

for key,data in users.items():
    print key
    i=1
    for value in users[key]:
        first_name=value['first_name']
        last_name=value['last_name']
        length = len(first_name)+len(last_name)
        print i, "- ", value['first_name'].upper(), value['last_name'].upper(), "- ",str(length)
        i=i+1
