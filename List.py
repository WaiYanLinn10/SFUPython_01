List - []


word = 'Programming'


   p   r   o   g   r   a   m   m   i   n  g
  0    1   2   3   4   5   6   7   8   9  10
-11  -10  -9  -8  -7  -6  -5  -4  -3  -2 -1 


>>> word = 'Programming'
>>> word[0]
'P'
>>> word[3:5]
'gr'
>>> word[0:]
'Programming'
>>> word[7]
'm'
>>> word[-1]
'g'
>>> word[-11]
'P'
>>> word[3:]
'gramming'
>>> word[:9]
'Programmi'
>>> word[5:-3]
'amm'
>>> word[:2] + word[3:]
'Prgramming'


len(word)

# Len = Length

squarae = 'Square'
len(square)
len(word) + len(square)

>>> square = 'Square'
>>> len(square)
6
>>> len(word) + len(square)
17


cube = [10, 20, 30, 45, 50]
cube

>>> cube = [10, 20, 30, 45, 50]
>>> cube
[10, 20, 30, 45, 50]
>>> cube[0]
10
>>> cube[4]
50
>>> cube[3] = 40
>>> cube
[10, 20, 30, 40, 50]
>>> cube[5] = 60
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list assignment index out of range
>>> cube.append(60)
>>> cube
[10, 20, 30, 40, 50, 60]
>>> cube.append(40+5+20+10)
>>> cube
[10, 20, 30, 40, 50, 60, 75]
>>> cube.reverse()
>>> cube
[75, 60, 50, 40, 30, 20, 10]
>>> cube.sort()
>>> cube
[10, 20, 30, 40, 50, 60, 75]
>>> cube.remove(75)
>>> cube
[10, 20, 30, 40, 50, 60]
>>> cube.pop()
60
>>> cube
[10, 20, 30, 40, 50]
>>> cube.pop()
50



cube1 = [10, 20, 30, 45, 50]
cube2 = [1, 2, 3, 4, 5]
cube1.extend(cube2)
cube1

del cube1[3]
del cube1[1:3]
del cube1[:]

programA = ['A','B','C','D','E']
programB = ['a','b','c','d','e']
programC = programA + programB
programC
['A', 'B', 'C', 'D', 'E', 'a', 'b', 'c' , 'd', 'e']
programD = [1, 2, 3, 4, 5]
programC = programC + programD
programC[9:] = []
programC[5:9] = programD
programC

len(ProgramC)

a = [10, 20, 30, 40, 50]
b = [60, 70, 80, 90, 100]
c = [110, 120, 130, 140, 150]
x = [a, b, c]
x

>>> x[0]
[10, 20, 30, 40, 50]

x[0][]
>>> x[0][]
  File "<stdin>", line 1
    x[0][]
         ^
SyntaxError: invalid syntax

x[][3]
>>> x[][3]
  File "<stdin>", line 1
    x[][3]
      ^
SyntaxError: invalid syntax

x[1][2]
>>> x[1][2]
80

x[1:2][1:2]
>>> x[1:2][1:2]
[]

x[][]
>>> x[][]
  File "<stdin>", line 1
    x[][]
      ^
SyntaxError: invalid syntax

x[0][0]
>>> x[0][0]
10

x[0][1:2]
>>> x[0][1:2]
[20]


>>> x[0:2][0]
[10, 20, 30, 40, 50]
>>> x[0:2][1]
[60, 70, 80, 90, 100]
>>> x[0:2][0][1]
20
>>> x[1:2][0][2]
80