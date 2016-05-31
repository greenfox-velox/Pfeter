# Create a `Stack` class that stores elements
# It should have a `size` method that returns number of elements it has
# It should have a `push` method that adds an element to the stack
# It should have a `pop` method that returns the last element form the stack and also deletes it from it

# please don`t use the built in methods
class Stack(object):
    def __init__(self):
        self.elements = []

    def size(self):
        elements_size = 0
        for i in self.elements:
            elements_size += 1
        return(elements_size)

    def push(self, element):
        self.elements += element

    def pop(self):
        elements_size = self.size()
        self.last_element = self.elements[elements_size - 1]
        temporary_list = []
        for shorter_i in range(elements_size):
            if shorter_i < (elements_size - 1):
                temporary_list += [self.elements[shorter_i]]
        self.elements = temporary_list
        return(self.last_element)

stack_1 = Stack()
print(stack_1.size())
stack_1.push(['thing1', 'thing2', 'thing3', 'thing4'])
print(stack_1.size())
print(stack_1.pop())
print(stack_1.size())
