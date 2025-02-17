


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


class AddingStacks(Stack):
    def __init__(self):
        Stack.__init__(self)
        self.__sum = 0

    def get_sum(self):
        return self.__sum
    
    def push(self, val):
        self.__sum += val
        Stack.push(self, val)

    def pop(self):
        val = Stack.pop(self)
        self.__sum -= val
        return val

stack_object = AddingStacks()

for i in range(5):
    stack_object.push(i)

print(stack_object.get_sum())
print(stack_object)


for i in range(5):
    print(stack_object.pop())