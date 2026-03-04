# 1. Write a Python program to reverse a given string using slicing.

s=input("Enter a string:")

print(s[::-1])

# # output
# Enter a string:Mnajunadh
# hdanujanM


# 2. Write a Python program to print every alternate character from a given string using slicing.

s=input("Enter a string:")

print(s[::2])

# # output
# Enter a string:mukesh
# mks

# 3. Write a Python program to extract the middle three characters from a given string (assume the string length is odd and at least 3).

s=input("Enter a string :")

mid=len(s)//2
print(s[mid-1:mid+2])

# # output:
# Enter a string :abcde
# bcd

# 4. Write a Python program to reverse a list of integers using slicing without using loops or built-in reverse functions.

lst=list(map(int,input("Enter list elements:").split()))

print(lst[::-1])

# # output:
# Enter list elements:12 23 34 45 56 67
# [67, 56, 45, 34, 23, 12]

# 5. Write a Python program to remove the first and last characters from a given string using slicing
s=input("Enter a string:")

print(s[1:-1])

# output
# Enter a string:manjunadh
# anjunad

