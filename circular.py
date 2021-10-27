x1=[0,0,3,-1,0]
x2=[1,1,1,0,0]
print("Input 1: ",x1)
print("Input 2: ",x2)

lengthX1 = len(x1)
lengthX2 = len(x2)

for i in range(lengthX2-lengthX1):
  x1.append(0)
for i in range(lengthX1-lengthX2):
  x2.append(0)

id1 = []
id2 = []

for i in range(lengthX1):
  id1.append(i)
  id2.append(i)

id2.reverse()

print("Length of Output Seq: ",x1)
print()

for j in range(len(id1)):
  temp=id2[-1]
  id2.pop()
  id2.insert(0,temp)
  temp=0
  print("y{}=".format(j),end=" ")
  for i,j in zip(id1,id2):
    print("{}*{}".format(x1[i],x2[j]),end=" + ")
    temp+=x1[i]*x2[j]
  print(" = {}".format(temp))
