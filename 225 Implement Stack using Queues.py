from queue import SimpleQueue
class MyStack:

    def __init__(self):
        self.q1, self.q2 = SimpleQueue(), SimpleQueue()

    def push(self, x: int) -> None:
        self.q1.put(x)
        
    def pop(self) -> int:
        while True:
            x = self.q1.get()
            if self.q1.empty():
                self.q1, self.q2 = self.q2, self.q1
                return x
            else:
                self.q2.put(x)
        
    def top(self) -> int:
        while True:
            x = self.q1.get()
            self.q2.put(x)
            if self.q1.empty():
                self.q1, self.q2 = self.q2, self.q1
                return x
        
    def empty(self) -> bool:
        return self.q1.empty()
        
