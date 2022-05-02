# print all 0-150
for i in range(151):
    print(i)

# printall multiples of 5 from 5-1,000
for i in range(5, 1001, 5):
    print(i)

# #3 Print integers 1 to 100. If divisible by 5, print "Coding" instead. If divisible by 10, print "Coding Dojo".
for i in range(1, 101):
    if i % 5 == 0 and i % 10 == 0:
        print("coding dojo")
    elif i % 5 == 0:
        print("coding")
    else:
        print(i)

# add 0-500k and print sum
sum = 0
for c in range(1, 500001, 2):
    sum += c
print(sum)


# Countdown by Fours

def count_down_four():
    number = 2018
    while number > 0:
        print(number)
        number = number - 4


count_down_four()

# Flexible Counter
lowNum = 2
highNum = 9
multi = 3


for v in range(lowNum, highNum + 1):
    if v % multi == 0:
        print(v)
