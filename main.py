from stack import *
from queue1 import *
from recursion import *

food = Stack()
food.push('hamburger')
food.push('fries')
food.push('cake')
food.pop()
#you just ate the cake

dessert = Queue1()
dessert.enq('pie')
dessert.enq('cake')
dessert.enq('jello')
dessert.deq()
dessert.deq()

print(fact(5))
print(fib(19))

for x in range(100):
    print('fib({0})={1}'.format(x, fib(x)))
pass