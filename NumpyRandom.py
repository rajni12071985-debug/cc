from numpy import random

#x = random.randint(100 , size=(4,6))
#print(x)


y = random.rand(5)
print(y)

z = random.choice([2,6,14,18,1,2,3],size=(3,5))
print(z)

x = random.choice([3,14,18,9] , p = [0.1 , 0.6, 0.2, 0.1], size=(100))

print(x)

w = random.choice([3,14,18,9] , p = [0.1 , 0.6, 0.2, 0.1], size=(3,5))
print(w)

