import numpy as np 

a = np.array([[1,2,3,4],[5,6,7,8]])
print(a)

b = a.shape

print(b)
print(a[0,1])

print(type(a))
\

c = np.array([[[1,2,3,4],[5,6,7,8]] ,[[9,10,11,12],[13,14,15,16]]])

print(c[1,1,3])


d = np.array([0, 1.2 ,2.7] )

print(d)
print(d.dtype)
print(type(d))


newarr = d.astype(bool)
print(newarr)

x = d.copy()

d[0] = 24

print(d)
print(x)


x = d.view()

x[0] = 45 

print(d)
print(x)

print(d.shape)

y =  np.array([1,2,3,4] , ndmin = 5)

print(y.shape)

print(y.reshape(2,2))


p = np.array([1,2,3,4,5,6,7,8,9,10,11,12])

print(p.reshape(2,3,2))

g = np.array([[1,2,3] , [4,5,6]])

for r in g:
    for f in r:
        print(f)


s = np.array([[[1,2,3,4],[5,6,7,8]] , [[1,2,3,4] , [5,6,7,8]]])  
  
for In in s:
    for inn in In:
        for innn in inn:
            print(innn)



# High Dimensional Array

for j in np.nditer(s):
    print(j)


uni = np.array([1,2,3,4,5])

for i in np.nditer(uni,flags=['buffered'] , op_dtypes=['S']):
    print(i)




for i in np.nditer(uni[::2]):
    print(i)