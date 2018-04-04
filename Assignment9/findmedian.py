"""
Solves the runningmedian problem at Hackerrank
https://www.hackerrank.com/challenges/find-the-running-median/forum
Taylor He, Jacob Manzelmann, Thomas Osterman
I pledge my honor that I have abided by the Stevens Honor System.
"""
from heapq import heappush, heappop, heapify

"""
MinHeap is a wrapper around heapq
Min heaps are supported by negating the input on the max heap
"""
class MinHeap:
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
        return -self.heap[0] if len(self.heap) > 0 else None

    def __len__(self):
        """Returns the size of the heap"""
        return len(self.heap)

"""
MaxHeap is a wrapper around heapq
Max heaps are inherently supported by heapq
"""
class MaxHeap:
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
        return self.heap[0] if len(self.heap) > 0 else None

    def __len__(self):
        """Returns the size of the heap"""
        return len(self.heap)

def runningMedian(a):
    """
    runningMedian prints the median as it is traversing
    through list a
    This is done by maintaining 2 heaps of same size
        max_heap:   all items > med is added to this heap
        min_heap:   all items < med is added to this heap
    Also, absolute value of (len(max_heap) - len(min_heap)) >= 1
    The median is found by obtaining the top element in both heaps
    and finding the median of them
    """
    min_heap = MinHeap()
    max_heap = MaxHeap()
    res = []
    median = 0
    for item in a:
        if item > median:
            max_heap.push(item)
        else:
            min_heap.push(item)

        # balance the heaps by pushing and popping from the larger
        # to the smaller sized heap
        if len(min_heap) > len(max_heap) + 1:
            max_heap.push(min_heap.pop())
        elif len(max_heap) > len(min_heap) + 1:
            min_heap.push(max_heap.pop())

        # If heaps are same size, the median is the average   
        # of max of min_heap and min of max_heap
        # Else, it's top of the larger of the 2
        if len(min_heap) == len(max_heap):
            median = (min_heap.peek() + max_heap.peek()) / 2.0
        elif len(min_heap) > len(max_heap):
            median = float(min_heap.peek())
        else:
            median = float(max_heap.peek())
        
        # Prints with 1 decimal point
        res.append(round(median,1))
    return res

if __name__ == '__main__':
    a = []
    cases = int(raw_input())
    for i in range(cases):
        a_item = int(raw_input())
        a.append(a_item)

    result = runningMedian(a)
    print '\n'.join(map(str, result))
