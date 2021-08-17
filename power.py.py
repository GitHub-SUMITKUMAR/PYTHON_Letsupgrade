def power(x, y):
    if (y == 0):
        return 1
    if (x == 0):
        return 0
     
    return x * power(x, y - 1)
x =2
y = 3
 
print(power(x, y))