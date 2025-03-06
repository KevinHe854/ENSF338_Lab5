# Question 5
# It seems that an array implementation of stacks is more efficient than the linked list implementation. This is because Python already has methods for pushing and pooping from arrays, whereas we would have to create our own push and pop for linked lists.

import timeit
import random
from matplotlib import pyplot as plt

class ArrayStack:
    def __init__(self):
        self._stack = [generate_random_list() for i in range(0, 100)]
    
    def push(self, num):
        self._stack.append(num)
    
    def pop(self):
        if len(self._stack) == 0:
            return None
        
        return self._stack.pop()

class LLStack:
    def __init__(self):
        self._head = None
        for i in range(0, 100):
            self._head = Node(generate_random_list(), self._head)
    
    def push(self, num):
        self._head = Node(num, self._head)
    
    def pop(self):
        if self._head is None:
            return None
        
        temp = self._head.getData()
        self._head = self._head.getNext()
        return temp

class Node:
    def __init__(self, data, next=None):
        self._data = data
        self._next = next
    
    def getData(self):
        return self._data
    
    def setData(self, data):
        self._data = data
    
    def getNext(self):
        return self._next
    
    def setNext(self, next):
        self._next = next

def generate_random_list():
    return random.randint(1, 100)

def generate_random_tasks():
    return [random.randint(0, 9) for i in range(0, 10000)]

def main():
    a_setup = '''
from __main__ import ArrayStack
from __main__ import generate_random_list
from __main__ import generate_random_tasks
myArrayStack = ArrayStack()
myTasks = generate_random_tasks()
    '''
    ll_setup = '''
from __main__ import LLStack
from __main__ import generate_random_list
from __main__ import generate_random_tasks
myLLStack = LLStack()
myTasks = generate_random_tasks()
    '''
    
    a_stmt = '''
for i in myTasks:
    if i < 7:
        myArrayStack.push(generate_random_list())
    else:
        myArrayStack.pop()
    '''
    ll_stmt = '''
for i in myTasks:
    if i < 7:
        myLLStack.push(generate_random_list())
    else:
        myLLStack.pop()
    '''
    
    a_times = timeit.repeat(setup=a_setup, stmt=a_stmt, repeat=100, number=1)
    ll_times = timeit.repeat(setup=ll_setup, stmt=ll_stmt, repeat=100, number=1)
    
    plt.hist(a_times, color='r', alpha=0.5, label='ArrayStack')
    plt.hist(ll_times, color='b', alpha=0.5, label='LLStack')
    
    plt.title('Performance of Array vs Linked List Implementation of Stacks')
    plt.xlabel('Time (seconds)')
    plt.ylabel('Distribution')
    
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()