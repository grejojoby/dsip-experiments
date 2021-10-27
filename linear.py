h=list(map(int,input().split()))
x=list(map(int,input().split()))
lengthH = len(h)
lengthX = len(x)
n= lengthH + lengthX - 1

def getValue(a,y):
    if 0<=y<len(a):
        return a[y] 
    else:
        return 0

outputList=[]

for i in range(n):
    t=0
    for k in range(len(h)):
        t+=getValue(x,k)*getValue(h,i-k)
    outputList.append(t)

print(outputList)
