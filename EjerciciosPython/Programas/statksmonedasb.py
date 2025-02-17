

import sys


class Stack:
    def __init__(self):
        self.size = 0
        self.___stack_list = []

    def push( self, val):
        self.___stack_list.append(val)
        self.size += 1

    def pop(self):
        val = self.___stack_list[-1]
        del self.___stack_list[-1]
        self.size -=1
        return val
    def __str__(self):
        print(f"Pila = {self.___stack_list}")

stack_object = Stack()
stack_object.push(3)
stack_object.push(2)
stack_object.push(1)

print(stack_object.pop()) 
print(stack_object.pop())
print(stack_object.pop())  

try:
        print(len(stack_object.stack_list))
except AttributeError:
     print("Error")
     sys.exit(1)
