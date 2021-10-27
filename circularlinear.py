x1=[2,1,-2]
x2=[1,2,-1]
print("Input 1: ",x1)
# x1 = list(map(int,input().split(",")))
print("Input 2: ",x2)
# x2 = list(map(int,input().split(",")))
lengthX1 = len(x1)
lengthX2 = len(x2)
n = lengthX1 + lengthX2 - 1

for i in range(n-lengthX1):
  x1.append(0)
for i in range(n-lengthX2):
  x2.append(0)

id1 = []
id2 = []

for i in range(lengthX1):
  id1.append(i)
  id2.append(i)

id2.reverse()

print("Length of Output Seq: ",n)
print()

for j in range(n): 
  temp=id2[-1]
  id2.pop()
  id2.insert(0,temp)
  temp=0
  print("y{}=".format(j),end=" ")
  for i,j in zip(id1,id2):
    print("{}*{}".format(x1[i],x2[j]),end=" + ")
    temp+=x1[i]*x2[j]
  print(" = {}".format(temp))



