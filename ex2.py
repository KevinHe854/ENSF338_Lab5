# Question 5
# The second implementation is faster because in the first implementation, whenever we initialize or enqueue in the first array, we are calling merge sort which has O(n long n) complexity, while in the second we are simply inserting the element where it belongs in order, which has O(n) complexity. Since O(n) is more efficient than O(n log n), the second way is faster than the first.

import timeit
import random

class PriorityQueue1:
    def __init__(self):
        self._queue = [generate_random_list() for i in range(0, 100)]
        self.merge_sort(0, len(self._queue) - 1)

    def enqueue(self, num):
        self._queue.append(num)
        self.merge_sort(0, len(self._queue) - 1)
        
    def dequeue(self):
        if len(self._queue) == 0:
            return None
        
        temp = self._queue[0]
        self._queue.remove(temp)
        return temp
    
    def merge_sort(self, low, high):
        if low < high:
            mid = (low + high) // 2
            self.merge_sort(low, mid)
            self.merge_sort(mid+1, high)
            self.merge(low, mid, high)
    
    def merge(self, low, mid, high):
        size_left = mid - low + 1
        size_right = high - mid
        
        # Add elements into left and right subarrays
        left_subarr = [0] * size_left
        right_subarr = [0] * size_right
        
        for i in range(0, size_left):
            left_subarr[i] = self._queue[low + i]
            
        for j in range(0, size_right):
            right_subarr[j] = self._queue[mid + 1 + j]
            
        # Merge subarrays
        index_left = 0
        index_right = 0
        index_arr = low
        
        while index_left < size_left and index_right < size_right:
            if left_subarr[index_left] <= right_subarr[index_right]:
                self._queue[index_arr] = left_subarr[index_left]
                index_left += 1
            else:
                self._queue[index_arr] = right_subarr[index_right]
                index_right += 1
            index_arr += 1
            
        # If right_subarr is all done, finish left_subarr
        while index_left < size_left:
            self._queue[index_arr] = left_subarr[index_left]
            index_left += 1
            index_arr += 1
            
        # If left_subarr is done, finish right_subarr
        while index_right < size_right:
            self._queue[index_arr] = right_subarr[index_right]
            index_right += 1
            index_arr += 1

class PriorityQueue2:
    def __init__(self):
        self._queue = []
        for i in range(0, 100):
            temp = generate_random_list()
            self.insert(temp)
    
    def enqueue(self, num):
        self.insert(num)
    
    def dequeue(self):
        if len(self._queue) == 0:
            return None
        
        temp = self._queue[0]
        self._queue.remove(temp)
        return temp
    
    def insert(self, num):
        index = len(self._queue)
        
        # Expand array by 1
        self._queue.append(None)
        
        # Start at the end
        while True:
            # Reached the beginning
            if index == 0:
                self._queue[index] = num
                break

            # Insert the new number
            elif self._queue[index - 1] <= num:
                self._queue[index] = num
                break
            
            # Shift elements greater than num to the right by 1
            else:
                self._queue[index] = self._queue[index - 1]
                index -= 1

def generate_random_list():
    return random.randint(1, 100)

def generate_random_tasks():
    return [random.randint(0, 9) for i in range(0, 1000)]

def main():
    q1_setup = '''
from __main__ import PriorityQueue1
from __main__ import generate_random_list
from __main__ import generate_random_tasks
myPriorityQueue1 = PriorityQueue1()
myTasks = generate_random_tasks()
    '''
    q2_setup = '''
from __main__ import PriorityQueue2
from __main__ import generate_random_list
from __main__ import generate_random_tasks
myPriorityQueue2 = PriorityQueue2()
myTasks = generate_random_tasks()
    '''
    
    q1_stmt = '''
for i in myTasks:
    if i < 7:
        myPriorityQueue1.enqueue(generate_random_list())
    else:
        myPriorityQueue1.dequeue()
    '''
    q2_stmt = '''
for i in myTasks:
    if i < 7:
        myPriorityQueue2.enqueue(generate_random_list())
    else:
        myPriorityQueue2.dequeue()
    '''
    
    q1_time = min(timeit.repeat(setup=q1_setup, stmt=q1_stmt, repeat=100, number=1))
    q2_time = min(timeit.repeat(setup=q2_setup, stmt=q2_stmt, repeat=100, number=1))
    
    print('PriorityQueue1 time to complete tasks is {} seconds'.format(q1_time))
    print('PriorityQueue2 time to complete tasks is {} seconds'.format(q2_time))

    # myPriorityQueue1 = PriorityQueue1()
    # myPriorityQueue2 = PriorityQueue2()
    # myTasks = generate_random_tasks()
    
    # for i in myTasks:
    #     if i < 7:
    #         myPriorityQueue1.enqueue(generate_random_list())
    #     else:
    #         myPriorityQueue1.dequeue()

if __name__ == "__main__":
    main()