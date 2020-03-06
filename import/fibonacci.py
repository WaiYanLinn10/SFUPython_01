#fibonacci.py

#Fibonacci numbers module

#n = int(input('Please enter a number: '))

def fib(n): 	#write Fibonacci series up to n
	a, b = 0, 1
	while a < n:
		print(a, end=' ')
		a, b = b, a+b
	print()

# #>>> fib(200)
# 0 1 1 2 3 5 8 13 21 34 55 89 144

#Go to Fibonnacci Powerpoint

def fib2(n): 	#return Fibonnaci series up to n 
	result = []
	a, b = 0, 1
	while a < n:
		result.append(a)
		a, b = b, a+b 
	return result

# >>> fib2(200)
# [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]