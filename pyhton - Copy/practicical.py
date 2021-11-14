# -*- coding: utf-8 -*-
"""
This is a practical for python
"""
# five is greater than two


if 5 > 2:
    print("five is greater than two")

# Working on Variables


x = 5
y = "john"
print(x)
print(y)

# string variables
x = str(3)
y = int(3)
z = float(3)

x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)
print("hello world ")

# this is a mathematical Operator

x = 3
y = 20
print(x + y)

# this is a global  operator 

x = "awesome"


def myfunc():
    print("Python is " + x)


myfunc()

# global  operator 2

x = "awesome"


def myfunc():
    x = "fantastic"
    print("Python is " + x)


myfunc()

print("Python is " + x)

if 10 < 12:
    print("false")

# variables
a, b, c = "beans", "orange", "cake"
print(b)
print(a)
print(c)

# for statement

for x in "banana":
    print(x)

# the if statement

a = 12
b = 200
if b > a:
    print("b is greater than a")

# The elif keyword

a = 20
b = 20
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")
exit()
