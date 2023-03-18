def __init__(self, homepage: str):
    self.m = 0   # max history
    self.i = 0   # current position
    self.arr = [None] * 5000
    self.arr[0] = homepage
    
def visit(self, url: str) -> None:
    self.i += 1
    self.arr[self.i] = url
    self.m = self.i

def back(self, steps: int) -> str:
    self.i = max(0, self.i-steps)
    return self.arr[self.i]

def forward(self, steps: int) -> str:
    self.i = min(self.i+steps, self
