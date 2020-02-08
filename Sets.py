#sets

Set.py

includes a data type for sets.
Curly braces {} or the set () function can be used to create sets.

basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)		# show that duplicates have been removed

'orange' in basket					#fast membership testing
'crabgrass' in basket

Demonstrate set operations on unique letters from two words

a = set('abracadabra')
b = set('alacazam')
a 								# unique letters in a 
a - b 							# letters in a but not in b
a | b 							# letters in a or b or both
a & b 							# letters in both a and b
a ^ b 							# letters in a or b but not both

a = {x for x in 'abracadabra' if x not in 'abc'}
a


x = set('23802348')
y = set('57839012')
x - y
y - x
x ^ y 
y | x
x & y

-------

fruits = {"apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"}
print("cherry" in fruits)

fruits.add ("cucumber")
fruits
fruits.update("grape")
fruits
fruits.remove("banana")
fruits
fruits.discard("kiwi")
fruits

>>>Dictionaries

#Dictionaries

#Another useful data type built into Python is the dictionary

tel = {'jack': 4098, 'sape': 4139}
tel['sape']
tel['guido'] = 4127
tel

list(tel) #Change to list

sorted(student) #Alphabet Sorting

'MgOo' in student

'MaMa' not in student

-----------

dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
dict(sape=4139, guido=4127, jack=4098)

{x: x**2 for x in (2, 4, 6)}

for x in 2, 4, 6:
	print(x, ':', x **2)

2:4
4:16
6:36

>>> for x in 2, 4, 6:
...     print(x, ':', x **2)
...
2 : 4
4 : 16
6 : 36

----------
When looping through dictionaries

knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
	print(k, v)

	k = key
	v = value