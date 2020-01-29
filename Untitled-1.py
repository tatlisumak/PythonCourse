"""liste = [1,1]
for i in range(2,10):
    liste.append(liste[i-1]+liste[i-2])
print(liste)

list1=[1,1]
while len(list1) < 10:
    list1.append(list1[-1]+list1[-2])



print(list1)"""

def fib(n):
    list1=[1,1]
    while len(list1) < n:
        list1.append(list1[-1]+list1[-2])
    return list1

print(fib(5))
