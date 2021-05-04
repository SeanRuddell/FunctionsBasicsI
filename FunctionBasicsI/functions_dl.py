#1
def number_of_food_groups():
    return 5
print(number_of_food_groups())
# output will print 5

#2
def number_of_military_branches():
    return 5
print(number_of_days_in_a_week_silicon_or_triangle_sides() + number_of_military_branches())
# will print an error since the first function is not defined

#3
def number_of_books_on_hold():
    return 5
    return 10
print(number_of_books_on_hold())
# will print the output 10 since that was the last value returned to the function
# *correction* it will print out 5 because 'return" stops the continuation of the function until called again

#4
def number_of_fingers():
    return 5
    print(10)
print(number_of_fingers())
# output will be 5

#5
def number_of_great_lakes():
    print(5)
x = number_of_great_lakes()
print(x)
# out will be 5; line 29 it is defined, line 30 states what the function will execute, line 31 defines x as the new variable for the functions output, line 32 calls the functions to print
# *correction* nothing is being returned to the function, nothing is printed

#6
def add(b,c):
    print(b+c)
print(add(1,2) + add(2,3))
#prints the new values from when the function is called ("add") 3 and 5

#7
def concatenate(b,c):
    return str(b)+str(c)
print(concatenate(2,5))
#prints the returned integers as strings together as a list "25"

#8
def number_of_oceans_or_fingers_or_continents():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(number_of_oceans_or_fingers_or_continents())
# when functions is called, will print value b  , and the condition isnt met so we return 10 from else
# output should be "100 10"

#9
def number_of_days_in_a_week_silicon_or_triangle_sides(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3) + number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
"""
line 68's arguments meet the condition so 7 is returned and printed
line 69's arguments don't meet the condition so the else condition is applied and we return 14
line 70's call is adding the integers after the function is performed twice to get print('7 + 14') to get 21
output should be:
7
14
21
"""

#10
def addition(b,c):
    return b+c
    return 10
print(addition(3,5))
# once returned we take the returned value and end the loop and return to the top (b+c) or 3+5 = 8

#11
b = 500
print(b)
def foobar():
    b = 300
    print(b)
print(b)
foobar()
print(b)
# should print out 500, 500, 300, 500 as print(b) is called three times and is defined outside the function. When the function is then called it takes the variable b and prints that value. It never returns the value.

#12
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
foobar()
print(b)
# should print out 500, 500, 300, 300, 500. We have three print(b)'s outside the function that are set to 500. Within the function foobar, we print the value within the function 300 and then we return the value b to the function; the other 300

#13
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
b=foobar()
print(b)
# should print out 500, 500, 300, 300. The first two print(b)'s print the value of b 500. line 119 b=foobar() sets b to the function now. line 120 calls the function to be printed and within the function we print b @ value 300 and it is returned at 300

#14
def foo():
    print(1)
    bar()
    print(2)
def bar():
    print(3)
foo()
# output should be 1, 3, 2. foo is defined and bar is defined. last line calls for function foo. In the function we print '1' then call the function bar, which is to print '3', and then we finished out the function foo by printing 3

#15
def foo():
    print(1)
    x = bar()
    print(x)
    return 10
def bar():
    print(3)
    return 5
y = foo()
print(y)
"""
output should be 1, 3, 5, 10; 
where foo() produces 1, 3, 5
and print(y) (printing the value of y which was just set to the function foo()) outputs 10
"""
