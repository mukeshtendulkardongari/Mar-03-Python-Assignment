# 1. Check if a Matrix is Square
l=[[1, 2],
   [3, 4]]

rows=len(l)
cols=len(l[0])

print(rows==cols)

# output:
# True

# 2. Print Diagonal Elements

l=[[1, 2],
   [3, 4]]
d=[]
for i in range(len(l)):
    for j in range(len(l[i])):
        if i==j:
            d.append(l[i][j])
print(d)

# output:
# [1, 4]

# 3. Print Anti-Diagonal Elements

l=[[1, 2],
   [3, 4]]
anti=[]
for i in range(len(l)):
    for j in range(len(l[i])):
        if i+j==len(l)-1:
            anti.append(l[i][j])
print(anti)

# output:
# [2, 3]

# 4. Print Non-Diagonal Elements

l=[[1, 2],
   [3, 4]]
non_d=[]
for i in range(len(l)):
    for j in range(len(l[i])):
        if i!=j:
            non_d.append(l[i][j])
print(non_d)

# output:
# [2, 3]

# 5. Print Non-Anti-Diagonal Elements

l=[[1, 2],
   [3, 4]]
non_anti=[]
for i in range(len(l)):
    for j in range(len(l[i])):
        if i+j!=len(l)-1:
            non_anti.append(l[i][j])
print(non_anti)

# output:
# [1, 4]

# 6. Lower Triangle of Matrix

l=[[1, 2],
   [3, 4]]

n = len(l)

for i in range(n):
    for j in range(n):
        if i>=j:
            print(l[i][j],end=" ")
        else:
            print(0,end=" ")
    print()

# output:
# 1 0 
# 3 4 

# 7. Upper Triangle of Matrix

l=[[1, 2],
   [3, 4]]

n = len(l)
for i in range(n):
    for j in range(n):
        if i<=j:
            print(l[i][j],end=" ")
        else:
            print(0,end=" ")
    print()

# # output:
# 1 2 
# 0 4 

# 8. Transpose of Matrix

l=[[1, 2, 5],
   [3, 4, 9]]

rows = len(l)
cols = len(l[0])

for i in range(cols):
    for j in range(rows):
        print(l[j][i],end=" ")
    print()

# output:
# 1 3 
# 2 4 
# 5 9

# 9. Check if Diagonal Elements are Same

l=[[1, 2],
   [3, 4]]

first = l[0][0]
n=len(l)
f=True
for i in range(n):
    if l[i][i]!=first:
        f=False
        break
if f:
    print("All diagonal elements are same")
else:
    print("Diagonal elements are not same")

# output:
# Diagonal elements are not same


# 10. Check if Anti-Diagonal Elements are Same

l=[[1, 2],
   [3, 4]]

n=len(l)
first=l[0][n-1]
f=True
for i in range(n):
    if l[i][n-1-i]!=first:
        f=False
        break
if f:
    print("All anti diagonal elements are same")
else:
    print("Anti diagonal elements are not same")

# output:
# Anti diagonal elements are not same


# 11. Convert Diagonal Elements to Zero

l=[[1, 2],
   [3, 4]]

n=len(l)

for i in range(n):
    l[i][i]=0

print(l)

# ouput:
# [[0, 2], [3, 0]]

# 12. Convert Anti-Diagonal Elements to Zero

l=[[1, 2],
   [3, 4]]

n=len(l)

for i in range(n):
    l[i][n-1-i]=0

print(l)

# output:
# [[1, 0], [0, 4]]

# 13. Convert Non-Diagonal Elements to Zero

l=[[1, 2, 3],
   [4, 5, 6],
   [7, 8, 9]]

n=len(l)

for i in range(n):
    for j in range(n):
        if i!=j:
            l[i][j]=0
print(l)

# output:
# [[1, 0, 0], [0, 5, 0], [0, 0, 9]]

# 14. Sum of All Elements in Matrix

l=[[1, 2],
   [3, 4]]

sum_m=0
for i in range(len(l)):
    for j in range(len(l[i])):
        sum_m+=l[i][j]
print(sum_m)

# output:
# 10

