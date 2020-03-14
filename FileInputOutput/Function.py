def say_hello():
	print('Hello World')


say_hello()


#function_parameter

def print_max(a,b):
	if a > b:
		print(a,' is maximum')
	elif a == b:
		print(a,' is equal to', b)
	else:
		print(b,'is maximum')


#Local Variables

def func(x):
	print('x is',x)
	x = 2
	print('Changed local x to',x)

x = 50
func(x)
print('x is still',x)

x = 30

def func(x):
	x = 2

def funx(x)
	x = 10


#Global Statement

def func():
	global x

	print('x is',x)
	x = 2
	print('Changed global x to',x)

x = 50
func()
print('value of x is',x)

# >>> def exam_result(x):
# ...     if x < 101 and x > 89 or x == 100:
# ...             print("A")
# ...     elif x <= 89 and x > 79:
# ...             print("B")
# ...     elif x <= 79 and x > 59:
# ...             print("C")
# ...     elif x <= 59 and x > 49:
# ...             print("D")
# ...     elif x <= 49 and x > 0 or x == 0:
# ...             print("F")
# ...     else:
# ...             print("Check Again")
# ...
# >>> exam_result(80)
# B

# >>> def exam_result1():
# ...     x = int(input("Please enter your number: "))
# ...     if x < 101 and x > 89 or x == 100:
# ...             print("A")
# ...     elif x <= 89 and x > 79:
# ...             print("B")
# ...     elif x <= 79 and x > 59:
# ...             print("C")
# ...     elif x <= 59 and x > 49:
# ...             print("D")
# ...     elif x <= 49 and x > 0 or x == 0:
# ...             print("F")
# ...     else:
# ...             print("Check Again")
# ...
# >>> exam_result1()
# Please enter your number: 12
# F

def say(message, times=1):
	print(message * times )

say('hello')
say('World', 5)
say('Good Bye')


#Keyword Argument

def func(a, b=5, c=10):
	print('a is',a,'and b is',b, 'and c is', c)

func(3,8)
func(24, c=26)
func(c=20,a=39)


# >>> def func1(a,b=5,c=6):
# ...     print('a is {0}.b is {1}.c is {2}',format(a,b,c))
# ...
# >>> func(3,8)
# a is 3 and b is 8 and c is 10

#VarArgs parameters
#function_VarArgs.py

def total(a=5, *numbers,	**phonebook):
	print('a',a)

	for single_item in numbers:
		print('single_item',single_item)

	for first_part,second_part in phonebook.items():
		print(first_part,second_part)


total (10, 1, 2, 3,Jack=1123,John=2231,Inge=1459)

# >>> total (10, 1, 2, 3,Jack=1123,John=2231,Inge=1459)
# a 10
# single_item 1
# single_item 2
# single_item 3
# Jack 1123
# John 2231
# Inge 1459
# >>> total (10,326,40,58,0,99,1,2,3,Jack=1123,John=2231,Inge=1459)
# a 10
# single_item 326
# single_item 40
# single_item 58
# single_item 0
# single_item 99
# single_item 1
# single_item 2
# single_item 3
# Jack 1123
# John 2231
# Inge 1459


#Return statement

def maximum(x, y):
	if x > y:
		return x
	elif x == y;:
		return 'The numbers are equal'
	else:
		return y

maximum(3,8)
print(maximum(3,8))
print(maximum(20,10))

def max(x):
	x = 50
	return x

x = 20
max(x)
print(max(x))

#DocString (Documentation Strings)

def print_max(x, y):
	'''Prints the maximum of two numbers
		The Two values must be integers.
	'''
# (must enter)
	x = int(x)
	y = int(y)
	
	if x > y:
		print(x, 'is maximum')
	elif x < y:
		print(y, 'is maximum')
	else:
		print(x,'&',y,'is equal')



print_max(5,9)

print(print_max.__doc__)


def paper():
	'''1. There will be situations where your
	program has to interact with the users.
	For example, you would want to take input 
	from the user and then print some results
	back. We can achieve this using the input()
	function and print function respectively. '''

	'''2. There will be situation where your 
	program has to interact with users.
	For example, you would want to take input
	from the user and then print some resutls
	back. We cn achieve this using the input()
	Function and print function respectively. '''


print(paper.__doc__)