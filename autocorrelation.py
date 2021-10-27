import numpy as np

x = [1,2,3,4]
y = [5,6,7,8]

#auto
print("Auto Correlation")
yy = y.reverse()
res = [ [ 0 for i in range(len(x)) ] for j in range(len(y)) ]
for i in range(len(x)):
    for j in range(len(y)):
        res[j][i] = (x[i]*y[j])
for i in range(len(x)):
    for j in range(len(y)):
        print(res[i][j],end=" \t")
    print()

ans = [0] * (len(x)+len(y)-1)
for i in range(len(res)):
    for j in range(len(res[i])):
        ans[i+j] += res[i][j]

print(ans)

# #cross
print("Cross Correlation")
x = [0,1,-2,3,-4]
y = [0.5,1,2,1,0.5]
res = [ [ 0 for i in range(len(x)) ] for j in range(len(y)) ]
for i in range(len(x)):
    for j in range(len(y)):
        res[j][i] = (x[i]*y[j])
for i in range(len(x)):
    for j in range(len(y)):
        print(res[i][j],end=" \t")
    print()

ans = [0] * (len(x)+len(y)-1)
for i in range(len(res)):
    for j in range(len(res[i])):
        ans[i+j] += res[i][j]

print(ans)

# delayed cross
print("Delayed Cross Correlation")
x = [0,1,-2,3,-4]
y = [0.5,1,2,1,0.5]
delayX = int(input("Enter delayed position in X: "))
delayY = int(input("Enter delayed position in Y: "))
res = [ [ 0 for i in range(len(x)) ] for j in range(len(y)) ]
for i in range(len(x)):
    for j in range(len(y)):
        res[j][i] = (x[i]*y[j])
for i in range(len(x)):
    for j in range(len(y)):
        print(res[i][j],end=" \t")
    print()

ans = [0] * (len(x)+len(y)-1)
delayedPos = 0
for i in range(len(res)):
    for j in range(len(res[i])):
        ans[i+j] += res[i][j]
        if(i==delayX and j==delayY):
            delayedPos = i+j
print(ans)
print("Delayed Output Position: ",delayedPos)
print("Delayed Output Position Value: ",ans[delayedPos])
