
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
        keys = self._cases.keys()
        for k in keys:
            if m == k:
                return self._cases[k]
        return self._cases['default']
