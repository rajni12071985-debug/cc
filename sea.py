
import matplotlib.pyplot as plt

import seaborn as sns

from numpy import random

#sns.displot([0,1,2,3,4] , kind = "kde")

#plt.show()

#nn = random.normal(loc = 1 , scale = 2 , size=(2,3))

#print(nn)

# sns.displot(random.normal(size=100),kind = "kde")
# #plt.show()

# x = random.binomial(n=10 , p=0.5 , size = 10)

# print(x)


#x =[1,2,3,4]
#y=[1,2,3,4]

#c =["red"]

#plt.bar(x,y,color=c,width=0.1)
#plt.show()



# x =[1,8,5,7,3,4]
# y=[1.2,7.8,6,2,4,0]

# c =["red"]

# plt.title("pragati")

# plt.xlabel("month")
# plt.ylabel("final")

# plt.scatter(x,y,color=c)
# plt.show()


x =[1,8,5,7,3,4]
y=[1.2,7.8,6,2,4,0]


plt.title("pragati")

plt.xlabel("month")
plt.ylabel("final")

plt.plot(x,y,color="red")
plt.show()