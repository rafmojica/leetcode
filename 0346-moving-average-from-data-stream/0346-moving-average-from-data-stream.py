import collections

class MovingAverage:
    # 1. initialize window size and empty queue upon class creation
    # when next is called:
    # 2. if queue length is equal window size, popleft and append new val
    # 3. otherwise, add the val to queue
    # 4. return sum(queue) / queue length

    # without using sum() (faster)
    # 1. initialize window size, empty queue AND curr sum upon class creation
    # when next is called:
    # 2. if queue > size, save popleft, update currSum += val - popLeft
    # 3. add val to queue regardless, update currSum += val
    # 4. return currSum / len(queue)
    def __init__(self, size: int):
        self.size = size
        self.queue = collections.deque()
        self.currSum = 0

    def next(self, val: int) -> float:
        if len(self.queue) == self.size:
            leftmostVal = self.queue.popleft()
            self.currSum += val - leftmostVal
        else:
            self.currSum += val
        
        self.queue.append(val)

        return self.currSum / len(self.queue)

# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)