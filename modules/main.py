# Do not modify these lines
__winc_id__ = '78029e0e504a49e5b16482a7a23af58c'
__human_name__ = 'modules'

# Add your code after this line

import this
import time
import math
from datetime import datetime
import sys
from greet import supergreeting

# 1. At the top of your main.py, import a module that prints the Zen of Python.
# 2. Write a function wait that takes one argument -- seconds (int) --
#  that uses a function in the time module to make the computer wait for that number of seconds, then returns nothing.
def wait(secs):
    time.sleep(secs)
    return


# print(wait(10))

# 3. Implement a function my_sin that takes one float as an argument and returns the sine of that float. Use the math module.
def my_sin(float):
    sine = math.sin(float)
    return sine


# print(my_sin(1.70))

# 4. Implement a function iso_now that takes no arguments and returns a string containing the current date and time up to the minute in the ISO 8601 format.
def iso_now():
    iso_today = datetime.now().isoformat()
    return iso_today[0:16]


# print(iso_now())

# 5. Implement a function platform that takes no arguments and returns a string that shows which platform we are on.
def platform():
    which_platform = sys.platform
    return which_platform

# print(platform)

# 6. write a function supergreeting_wrapper that takes the exact same type of argument, calls supergreeting with it and returns the result.
def supergreeting_wrapper(name: str):
    copy = supergreeting(name)
    return copy


print(supergreeting_wrapper("Bob"))
