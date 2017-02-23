
def case(param):
    def decorator(fun):
        fun.value = param
        return fun
    return decorator


class Switch(object):

    def __init__(self):
        self._cases = {}
        self._setup()

    def _setup(self):
        for el in dir(self):
            try:
                attr = getattr(self, el)
                if type(attr.value) is tuple or type(attr.value) is list:
                    for el in attr.value:
                        self._cases[el] = attr
                else:
                    self._cases[attr.value] = attr
            except:
                pass

    def match(self, m):
        if m in self._cases:
                return self._cases[m]
        return self._cases['default']
