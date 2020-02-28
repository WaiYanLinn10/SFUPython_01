#If Else Statements
If_Else_Statements

#Boolean Expression -> True or False

print(20 > 10)
print(20 == 10)
print(20 < 10)
print(bool("Hello World"))
print(bool(20))


Python Conditions

Equals						-> x == y
Not Equals					-> x != y
Less than					-> x <  y
Less than or equal to		-> x <= y
Greater than				-> x >  y
Greater than or equal to 	-> x >= y
Boolean OR 					-> x or y , x | y
Boolean AND 				-> x and y, x & y
Boolean NOT 				->  not x



if -
else -


#IF statement
>>> x = 70
>>> y = 60
>>> if x > y:
...     print("x is greater than y")
... else:
...     print("x is not greater than y")
...
x is greater than y


>>> if x < y:
...     print("x is greater than y")
... else:
...     print("x is not greater than y")
...
x is not greater than y

>>> if x > y:
...      print("x is greater than y")
... elif x >= y:
...      print("x is greater or euqal to y")
... elif y < x:
...     print("y is smaller than x")
... else:
...     print("x is nothing")
...
x is greater than y

>>> if x == y:
...     print("Answer 1")
... elif x < y:
...     print("Answer 2")
... elif x <= y:
...     print("Answer 3")
... else:
...     print("default")
...
default

#Else

x = 50
y = 150
if x > y:
	print("x is greater than y")
elif x == y:
	print("x and y are equal")
else:
	print("x is less than y")

>>> if x > y: print("x is greater than y")
... elif x == y: print("x and y are equal")
... else: print("x is less than y")
...
x is less than y

#Short Hand If

if x > y: print("x is greater than y")

>>> if x > y: print("x is greater than y")
...
x is greater than y

#Short Hand If...Else
x = 50
y = 150
	print(x) if x > y else print(y)

>>> x = 50
>>> y = 150
>>> print(x) if x > y else print(y)
150


#And is logical operator
x = 50
y = 40
z = 100
if x > y and z > x:
	print("All Conditionss are True")

>>> x = 50
>>> y = 40
>>> z = 100
>>> if x > y and z > x:
...     print("All Conditionss are True")
...
All Conditionss are True

if x < y and z > x:
	print("All Conditions are Ture")
else:
	print("Some Conditions are False")

>>> if x < y and z > x:
...     print("All Conditions are Ture")
... else:
...     print("Some Conditions are False")
...
Some Conditions are False

#Or is logical operator

x = 50
y = 40
z = 100
if x > y or z < y:
	print("one of the conditions is true")
elif x > y and z > y:
	print("All conditions are true")
else:
	print("nothing else")

>>> x = 50
>>> y = 40
>>> z = 100
>>> if x > y or z < y:
...     print("one of the conditions is true")
... elif x > y and z > y:
...     print("All conditions are true")
... else:
...     print("nothing else")
...
one of the conditions is true

if x > y and z > y and z > x:
	print("Answer 1")
elif x == y or z == y or z > y and x > y:
	print("Answer 2")
elif z > y and y < x or z > y:
	print("Answer 3")
else:
	print("default")

>>> if x > y and z > y and z > x:
...     print("Answer 1")
... elif x == y or z == y or z > y and x > y:
...     print("Answer 2")
... elif z > y and y < x or z > y:
...     print("Answer 3")
... else:
...     print("default")
Answer 1

>>> if x > y and z > y and x > z:
...     print("Answer 1")
... elif z > y and y < x or z > y:
...     print("Answer 2")
... elif z > y and y < x or z > y:
...     print("Answer 3")
... else:
...     print("default")
...
Answer 2


#Nested If is if statements in if statements

x = 50

if x > 10:
	print("x is ten")
	if x > 20:
		print("x is greater than 20")
	else:
		print("No,x is not greater than 20")

if x > 10 and x != 10 or x > 20:
	print("x is greater than 10 and 20")
else:
	print("x is greater than 10 & 20")




>>>Loops

if student
	if batch
		if gender
else
	not 

student = "SFU"
	batch = "3"
		gender = "male"


>>> student = "SFU"
>>> batch = "3"
>>> gender = "male"
>>> if student == "SFU":
...     print("I'm SFU student")
...     if batch == "3":
...             print("Yes,I'm from batch 3")
...             if gender == "male":
...                     print("I'm a boy")
...             else:
...                     print("I'm a girl")
...     else:
...             print("No,I'm form other batch")
... else:
...     print("I'm not SFU student")
