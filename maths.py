#Add implementation
def add(x,y):
	return x+y

#Substract implementation
def substract(x,y):
	return x-y	#On Master branch

#Multiply implementation
def multiply(x,y):
	return x*y	#On Bug456 branch

#Divide implementation
def divide(x,y):
	if y==0		#On Master branch
		return DIVIDE_BY_ERROR_0
	else
		return x/y

#Square implementation
def square(x):
	return x*x
