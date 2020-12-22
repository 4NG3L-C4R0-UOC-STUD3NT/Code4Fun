import traceback
import sys
from pprint import pprint

def call_function(f, recursion_level=2):
    if recursion_level:
        return call_function(f, recursion_level-1)
    else:
        return f()

def f():
    #traceback.print_stack(file=sys.stdout)
    return traceback.extract_stack(), traceback.format_stack()

def Add(a, b):
    return a + b, traceback.format_stack()

print('Calling f() directly:')
f()

print()
print('Calling f() from 3 levels deep:')
stack, formatted_stack = call_function(f)
pprint(formatted_stack)
print("===========================================")
pprint(stack)
print("===========================================")
_, formatted_stack = Add(4, 5)
pprint(formatted_stack)
