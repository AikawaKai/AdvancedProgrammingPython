from skins import *

class stack(metaclass=skin):
    def __init__(self, dim=10):
        self.dimension = dim
        self.top = 0
        self.data = []
    def is_empty(self): return self.top == 0
    def is_full(self): return self.top == (self.dimension-1)

    def __str__(self):
        return "Stack top :- {0} Stack dim :- {1} Stack data :- {2}".format(self.top, self.dimension, self.data)

if __name__ == "__main__":
    s = stack(5) # 5 is the stack dimension
    trend = True
    for i in range(-1,14):
        if s.is_empty():
            s.become({push}, {pop})
            trend = True
        elif s.is_full():
            s.become({pop}, {push})
            trend = False
        s.push(i) if trend else s.pop()
        print(s)
