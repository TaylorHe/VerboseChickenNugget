"""
Solves the runningmedian problem at Hackerrank
https://www.hackerrank.com/challenges/find-the-running-median/forum
Taylor He, Jacob Manzelmann, Thomas Osterman
I pledge my honor that I have abided by the Stevens Honor System.
"""
############### This bit is for hackerrank #############
#!/bin/python
# from __future__ import print_function

# import os
# import sys
########################################################
from heapq import heappush, heappop, heapify

"""
MaxHeap is a wrapper around heapq
Max heaps are supported by negating the input on the max heap
Negation is due to heap[0] returning the largest item
Because this is the small number heap, we need the largest element.
Negation will sort by the most negative element, which is in fact the "largest",
but we have to make sure to negate the pop() and peek() when returning values
"""
class MaxHeap:
    def __init__(self, h=[]):
        """ Constructor, optional list init parameter """
        self.heap = [-item for item in h]
        heapify(self.heap)

    def push(self, item):
        """Pushes item onto minheap"""
        heappush(self.heap, -item)

    def pop(self):
        """Pops and Returns the min item. Negates the negation"""
        return -heappop(self.heap)

    def peek(self):
        """Returns the smallest element"""
        try:
            return -self.heap[0]
        except Exception as e:
            raise e
        
    def __len__(self):
        """Returns the size of the heap"""
        return len(self.heap)

"""
MinHeap is a wrapper around heapq
heap[0] returns the smallest element in the heap
after heapify-ing, and that's exactly what we want
"""
class MinHeap:
    def __init__(self, h=[]):
        """ Constructor, optional list init parameter """
        self.heap = h
        heapify(self.heap)

    def push(self, item):
        """Pushes item onto MaxHeap"""
        heappush(self.heap, item)

    def pop(self):
        """Pops and returns the max item"""
        return heappop(self.heap)

    def peek(self):
        """Returns the smallest element"""
        try:
            return self.heap[0]
        except Exception as e:
            raise e
            
    def __len__(self):
        """Returns the size of the heap"""
        return len(self.heap)

def runningMedian(a):
    """
    runningMedian prints the median as it is traversing
    through list a
    This is done by maintaining 2 heaps of same size
        higher_val_heap:    all items > med is added to this heap
                            This is a MinHeap, since we want the 
                            smallest item of the max items
        lower_val_heap:     all items < med is added to this heap
                            This is a MaxHeap, since we want the
                            largest item of the min items
    The diff of the size of both is <= 1 at all times
    The median is found by obtaining the top element in both heaps
    and finding the median of them
    """

    lower_val_heap = MaxHeap()
    higher_val_heap = MinHeap()
    running_median_list = []
    median = 0
    for item in a:
        # If the item is > median, push it on the higher_val_heap
        # else push to lower_val_heap
        if item > median:
            higher_val_heap.push(item)
        else:
            lower_val_heap.push(item)

        # balance the heaps by pushing and popping from the larger
        # to the smaller sized heap
        if len(lower_val_heap) > len(higher_val_heap) + 1:
            higher_val_heap.push(lower_val_heap.pop())
        elif len(higher_val_heap) > len(lower_val_heap) + 1:
            lower_val_heap.push(higher_val_heap.pop())

        # If heaps are same size, the median is the average of 
        # the max of lower_val_heap and the min of higher_val_heap
        # Else, it's top of the larger of the 2
        if len(lower_val_heap) == len(higher_val_heap):
            median = (lower_val_heap.peek() + higher_val_heap.peek()) / 2.0
        elif len(lower_val_heap) > len(higher_val_heap):
            median = float(lower_val_heap.peek())
        else:
            median = float(higher_val_heap.peek())
        
        # Appends to return list foratted with 1 decimal point
        running_median_list.append(round(median,1))
    
    return running_median_list

if __name__ == '__main__':
    a = []
    cases = int(raw_input())
    for i in range(cases):
        a_item = int(raw_input())
        a.append(a_item)

    result = runningMedian(a)
    print '\n'.join(map(str, result))

############### This bit is for hackerrank #############
# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     a_count = int(raw_input())

#     a = []

#     for _ in xrange(a_count):
#         a_item = int(raw_input())
#         a.append(a_item)

#     result = runningMedian(a)

#     fptr.write('\n'.join(map(str, result)))
#     fptr.write('\n')

#     fptr.close()
########################################################
