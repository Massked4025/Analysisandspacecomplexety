

#Time complexety = O(logn with base2)

#Space complexety

def space(n):
    return n*(n+1)/2

print(space(2))
#Space complexety = Theta(1)

def sum(a):
    sum = 0
    for i in a:
        sum = sum+i
    return sum

array = [12, 4, 7, 9, 23]
print(sum(array))
#Space complexety = Theta(a)
#The space will increase in this due to array