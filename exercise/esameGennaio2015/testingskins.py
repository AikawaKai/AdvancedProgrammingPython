from skinObject import *

if __name__ == "__main__":
    s = stack(5)  # 5 is the stack dimension
    trend = True
    for i in range(-1, 14):
        if s.is_empty():
            s.become({push}, {pop})
            trend = True
        elif s.is_full():
            s.become({pop}, {push})
            trend = False
        s.push(i) if trend else s.pop()
        print(s)
