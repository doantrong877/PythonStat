#Basic
for x in range(150):
    print(x+1)

#Multiples of Five 
for x in range(0,1000,5):
    print(x + 5)

#Counting, the Dojo Way
for x in range(1,101):
    if x % 10 == 0:
        print("Coding Dojo")
    elif x % 5 == 0:
        print("Coding")
    else:
        print(x)

#Whoa. That Sucker's Huge
sum = 0
for x in range(1,500000,2):
    sum += x
print(sum)

#Countdown by Fours
for x in range(2018,1,-4):
    print(x)

#Flexible Counter
lowNum = 2
highNum = 9
mult = 3
while lowNum <= highNum:
    if lowNum % 3 == 0:
        print(lowNum)
    lowNum += 1