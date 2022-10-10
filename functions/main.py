# Do not modify these lines
__winc_id__ = '49bce82ef9cc475ca3146ee15b0259d0'
__human_name__ = 'functions'

# Add your code after this line

#Define these functions in main.py:

#1 greet: takes a name and returns a string in the format:

def greet(name):
    return f"Hello, {name}!"
    
print(greet("Bob"))

#2 add: takes three numbers (integers or floats) and returns their sum. Example:

def add(arg1, arg2, arg3):
    sum = (arg1 + arg2 + arg3)
    return (sum)

print(add(5, 3, 2))

#3 positive: takes a number (integer or float) and returns whether or not it is positive in the form of a boolean. 

def positive(number):
    outcome = number > 0
    return(outcome)

print(positive(50))
print(positive(-50))
print(positive(0))

# negative: takes a number (integer or float) and returns whether or not it is negative in the form of a boolean. 

def negative(number):
    outcome = number < 0
    return(outcome)

print(negative(50))
print(negative(-50))
print(negative(0))