# Question 5
# The implementation of queues is slow for both arrays and linked lists. Enqueuing in an array has complexity O(n) because every element has to be
# shifted to the right to insert a new element in index 0, but dequeuing has complexity O(1) sice we just pop the last element. On the other hand,
# enqueuing in a linked list has complexity O(1) because we simply insert the new node at the head. However, dequeuing has complexity O(n) because 
# we have to traverse through the whole linked list to reach the node just before the tail, then fetch the data in the tail node and set the tail 
# pointer to the node before it.

import timeit
import random
from matplotlib import pyplot as plt

class ArrayQueue:
    def __init__(self):
        self._queue = []
    
    def enqueue(self, num):
        self._queue.insert(0, num)
    
    def dequeue(self):
        if len(self._queue) == 0:
            return None
        else:
            return self._queue.pop()

class LLQueue:
    def __init__(self):
        self._head = None
        self._tail = self._head
    
    def enqueue(self, num):
        self._head = Node(num, self._head)
        
        # if LL is empty
        if self._tail is None:
            self._tail = self._head
    
    def dequeue(self):
        # if LL is empty
        if self._head is None:
            return None
        
        # if LL has one element
        elif self._head is self._tail:
            temp = self._tail.getData()
            self._head = None
            self._tail = None
            return temp
        
        current = self._head
        while current.getNext() is not self._tail:
            current = current.getNext()
        
        temp = self._tail.getData()
        self._tail = current
        self._tail.setNext(None)
        
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

def generate_random_num():
    return random.randint(0, 99)

def generate_random_tasks():
    return [random.randint(0, 9) for i in range(0, 10000)]

def main():
    
    a_setup = '''
from __main__ import ArrayQueue
from __main__ import generate_random_num
from __main__ import generate_random_tasks
myArrayQueue = ArrayQueue()
myTasks = generate_random_tasks()
    '''
    ll_setup = '''
from __main__ import LLQueue
from __main__ import generate_random_num
from __main__ import generate_random_tasks
myLLQueue = LLQueue()
myTasks = generate_random_tasks()
    '''
    
    a_stmt = '''
for i in myTasks:
    if i < 7:
        myArrayQueue.enqueue(generate_random_num())
    else:
        myArrayQueue.dequeue()
    '''
    ll_stmt = '''
for i in myTasks:
    if i < 7:
        myLLQueue.enqueue(generate_random_num())
    else:
        myLLQueue.dequeue()
    '''
    
    a_times = timeit.repeat(setup=a_setup, stmt=a_stmt, repeat=100, number=1)
    ll_times = timeit.repeat(setup=ll_setup, stmt=ll_stmt, repeat=100, number=1)
    
    plt.hist(a_times, color='r', alpha=0.5, label='ArrayQueue')
    plt.hist(ll_times, color='b', alpha=0.5, label='LLQueue')
    
    plt.title('Performance of Array vs Linked List Implementation of Queues')
    plt.xlabel('Time (seconds)')
    plt.ylabel('Distribution')
    
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()