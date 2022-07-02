
num1 = 42 #variable declaration
num2 = 2.3 #variable declaration
boolean = True #variable declaration
string = 'Hello World' #variable declaration
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] #List initialize
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} #Dictionary initialize
fruit = ('blueberry', 'strawberry', 'banana') #Tuples initialize
print(type(fruit)) #log statement
print(pizza_toppings[1]) #log statement
pizza_toppings.append('Mushrooms') # List add value
print(person['name']) #log statement 
person['name'] = 'George' #Dictionary change value
person['eye_color'] = 'blue' #Dictionary add value
print(fruit[2]) #log statement

if num1 > 45: #conditional if
    print("It's greater") #log statement
else: #conditional else
    print("It's lower") #log statement

if len(string) < 5: #conditional if
    print("It's a short word!") #log statement
elif len(string) > 15: #conditional else if
    print("It's a long word!") #log statement
else: #conditional else 
    print("Just right!") #log statement

for x in range(5): #for loop 
    print(x) #log statement
for x in range(2,5): #for loop start 2 stop 5
    print(x) #log statement
for x in range(2,10,3):  #for loop start 2 stop 10 imcrement 3
    print(x) #log statement
x = 0 #NameError: name <variable name> is not defined
while(x < 5): #while loop stop 4
    print(x) #log statement
    x += 1 #increment

pizza_toppings.pop() #List delete value
pizza_toppings.pop(1) #List access value delete value

print(person) #log statement
person.pop('eye_color') #Dictionary delete value
print(person) #log statement

for topping in pizza_toppings: #for loop
    if topping == 'Pepperoni': #conditional if
        continue #for loop continue
    print('After 1st if statement') #log statement
    if topping == 'Olives': #conditional if
        break  #for loop break

def print_hello_ten_times(): #function
    for num in range(10): #for loop start 0 stop 10
        print('Hello') #log statement

print_hello_ten_times() #print Hello 10 times

def print_hello_x_times(x): #function with x as parameter
    for num in range(x): #for loop stop at x
        print('Hello') #log statement

print_hello_x_times(4) #print Hello 4 times

def print_hello_x_or_ten_times(x = 10):  #function with x as parameter euqal to 10
    for num in range(x): #for loop stop at 10
        print('Hello') #log statement

print_hello_x_or_ten_times() #print Hello 10 times
print_hello_x_or_ten_times(4) #print Hello 4 times

#multiline comment
"""
Bonus section    
"""


#single line comment

# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)