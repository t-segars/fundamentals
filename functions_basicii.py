# 1

def countdown(num):
    newarr = []
    for i in range (num, 0, -1):
        newarr.append(num)
        print(num)
        num -= 1
    return newarr
countdown(20)

# 2

x = [1,2]
def print_and_return(x):
    v = x[0]
    b = x[1]
    print(v)
    return(b)
y = print_and_return(x)
print(y)

# 3

x = [1,2,3,4,5] 
def first_plus_length(x):
        return x[0] + len(x)
y = first_plus_length(x)
print (y)

# 4

x = [5,2,3,2,1,4]
def greater_than_second(x):
    newlist = []
    sum = 0
    for i in range (x[0], len(x)):
        if x[i] > x[1]:
            newlist.append(x[i])
            sum += 1
    print(sum)
    return newlist
y = greater_than_second(x)
print(y)


# 5


x = [6,2]
def this_length(x):
    newlist = []
    newlist.append(x[1])
    return newlist*x[0]
y = this_length(x)
print(y)