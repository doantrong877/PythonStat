# 1) Update Values in Dictionaries and Lists
x = [ [5,2,3], [10,8,9] ] 
x[1][0] = 15
print(x)
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
students[0]['lastname'] = "Bryan"
print(students[0])

sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
sports_directory["soccer"][0] = "Andres"
print(sports_directory["soccer"])

z = [ {'x': 10, 'y': 20} ]
z[0]["y"] = 30
print(z)

# 2) Iterate Through a List of Dictionaries
students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
def iterateDictionary(students):
    for i in range(len(students)):
        fname = students[i]["first_name"]
        lname = students[i]["last_name"]
        print(f"first_name - {fname}, last_name - {lname}")
iterateDictionary(students)

# 3) Get Values From a List of Dictionaries

def iterateDictionary2(key_name, some_list):
    for i in range(len(some_list)):
        val = some_list[i][key_name]
        print(f"{val}")
iterateDictionary2("first_name", students)
iterateDictionary2("last_name", students)

# 4) Iterate Through a Dictionary with List Values
dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}


def printInfo(some_dict):
    for key, val in some_dict.items():
        name = key.upper()
        size = len(val)
        print(f"{size} {name}")
        for i in range(size):
            print(val[i])
        print( " " )
printInfo(dojo)