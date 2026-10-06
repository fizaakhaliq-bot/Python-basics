# This is a simple Python script that prints a welcome message.
# for single line comments, we can use the hash symbol (#)
# for multi-line comments, we can use triple quotes (''' or """)
# strings can be enclosed in single or double quotes
print("welcome to python")
# integer can be used without quotes
print(2+5)
print("2+5")
print(2-5)
print(2/5)
print(2*-5)
print("-" * 20)
# if we dont use a blank space, the output will be concatenated
print("python" * 10)
print(" python "* 10)
# if we want a seprator between the output, we can use sep='or any seprator we want!
print(" python|"* 10)
x = 5 
y = 6.0
z = "hello"
print(x)
print(y)
print(z)
print(x,y,z)
print(x+y)# we can use only varirable name to print the value
# now we will use type function to check the type of the variable but type function will not print the value and type cannot be used individually it should be used with print function and fuction within fuction can be used in python
print(type(x))  # this will print the type of x 
print(type(y))  # this will print the type of y
print(type(z))  # this will print the type of z 
#in python we can give an instruction to store  any data in which type we want to store it that is called type casting'''
x = str(3)  # converting integer to string
y = int(2.0)  # converting float to integer
z = float(3)  # converting integer to float
print(x)  # this will print the value of x which is now a string
print(y)  # this will print the value of y which is now an integer
print(z)  # this will print the value of z which is now a floats
# variables can be overwriting
# we can assign a value to a variable and then change it later
nationality = "Pakistani"
print(nationality) # this will give output as Pakistani
nationality = "Pakistani"
nationality = "Indian"  # now it will overwrite the previous value qnd give output as Indian instead of Pakistani
print(nationality)
# python is also case sensitive so there are some ways to creat variables
# we can use underscore to separate words in a variable name
first_name = "John"
# 1) camel case 
myVariableName = "This is a variable"
# 2) snake case
my_variable_name = "This is a variable"
# 3) pascal case
MyVariableName = "This is a variable"
# assigning multiple variables in one line
a, b, c = "red", "green", "blue"
print(a)  # this will print red
print(b)  # this will print green
print(c)  # this will print blue
# complex numbers in python can be represented using 'j ' for the imaginary part
complex_number = 3 + 4j  # j is used to represent the imaginary part and 3 is the real part
