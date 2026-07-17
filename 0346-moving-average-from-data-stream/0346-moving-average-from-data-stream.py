import collections

class MovingAverage:
    # 1. initialize window size and empty queue when upon creation
    # when next is called:
    # 2. if queue length is greater than window size, popleft and append new val
    # 3. otherwise, add the val to queue
    # 4. return sum(queue) / queue length
    def __init__(self, size: int):
        self.size = size
        self.queue = collections.deque() 

    def next(self, val: int) -> float:
        if len(self.queue) == self.size:
            self.queue.popleft()
        self.queue.append(val)
        
        return sum(self.queue) / len(self.queue)

# [5, 4, 3, 2, 1, 1]

# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)