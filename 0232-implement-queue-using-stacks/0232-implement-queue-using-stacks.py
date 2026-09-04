class MyQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []
        self.front = None
        

    def push(self, x: int) -> None:
        if not self.stack1 and not self.stack2:
            self.front = x

        self.stack1.append(x)

        

    def pop(self) -> int:
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
                
        popped = self.stack2.pop()

        if self.stack2:
            self.front = self.stack2[-1]
        elif self.stack1:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
            self.front = self.stack2[-1]

        return popped

    def peek(self) -> int:
        return self.front
        

    def empty(self) -> bool:
        return len(self.stack2) == 0 and len(self.stack1) == 0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()