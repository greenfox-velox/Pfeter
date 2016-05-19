# Create a `Stack` class that stores elements
# It should have a `size` method that returns number of elements it has
# It should have a `push` method that adds an element to the stack
# It should have a `pop` method that returns the last element form the stack and also deletes it from it

# please don`t use the built in methods
class Stack(object):
    def __init__(self):
        self.elements = []

    def size(self):
        return(len(self.elements))

    def push(self, element):
        self.elements.append(element)

    def pop(self):
        self.last_element = self.elements[len(self.elements) - 1]
        self.elements.remove(self.elements[len(self.elements) - 1])
        return(self.last_element)

stack_1 = Stack()
print(stack_1.size())
stack_1.push('thing1')
stack_1.push('thing2')
stack_1.push('thing3')
stack_1.push('thing4')
print(stack_1.size())
print(stack_1.pop())
print(stack_1.size())
