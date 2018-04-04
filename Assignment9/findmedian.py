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
Negation is due to heap[0] returning the smallest item
Because this is the small number heap, we need the largest element.
Negation will sort by the "largest" element, but we have to make
sure to negate the pop() and peek() when returning value
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
        try:
            return -self.heap[0]
        except Exception as e:
            raise e
        
    def __len__(self):
        """Returns the size of the heap"""
        return len(self.heap)

"""
MaxHeap is a wrapper around heapq
heap[0] returns the smallest element in the heap
after heapify-ing, and that's exactly what we want
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
        max_heap:   all items > med is added to this heap
        min_heap:   all items < med is added to this heap
    Also, diff of the size of both is <= 1 at all times
    The median is found by obtaining the top element in both heaps
    and finding the median of them
    """
    min_heap = MinHeap()
    max_heap = MaxHeap()
    running_median_list = []
    median = 0
    for item in a:
        # If the item is > median, push it on the max_heap
        # else push to min_heap
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

        # If heaps are same size, the median is the average of 
        # the max of min_heap and the min of max_heap
        # Else, it's top of the larger of the 2
        if len(min_heap) == len(max_heap):
            median = (min_heap.peek() + max_heap.peek()) / 2.0
        elif len(min_heap) > len(max_heap):
            median = float(min_heap.peek())
        else:
            median = float(max_heap.peek())
        
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
