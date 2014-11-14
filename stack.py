__author__ = 'Shruti'
#double _ underscore are like hidden variables

class Stack:
    data = []
#made a class like a factory Stack
#food.push is an instance method and self is food
    def push(self, name):
        self.data.append(name)

    def pop(self):
        self.data.pop()


