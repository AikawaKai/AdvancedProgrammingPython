from itertools import permutations as perm
import re

class RiddleSolver():

    def __init__(self, riddle):
        self._riddle = riddle
        self._set = list(set(re.sub('[ +=]', '', self._riddle)))
        print(self._set)
        self._permutations = perm(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'], len(self._set))

    def __iter__(self):
        return self

    def __next__(self):
        cur = next(self._permutations)
        riddle_num = self._riddle
        notFound = True
        while notFound:
            for i in range(len(self._set)):
                riddle_num = re.sub(self._set[i], cur[i], riddle_num)
            try:
                if not eval(riddle_num):
                    cur = next(self._permutations)
                    riddle_num = self._riddle
                else:
                    notFound = False
            except:
                cur = next(self._permutations)
                riddle_num = self._riddle
        notFound = True
        return riddle_num

if __name__ == '__main__':
    riddle_solver = RiddleSolver("HAWAII + IDAHO + IOWA + OHIO == STATES")
    for sol in riddle_solver:
        print(sol)
