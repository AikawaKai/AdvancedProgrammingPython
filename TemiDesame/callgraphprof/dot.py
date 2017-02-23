from types import FunctionType
import inspect
import functools

class CG(type):
   def __new__(meta, classname, supers, classdict):
      changed = []
      for attr, attrval in classdict.items():
         if type(attrval) is FunctionType:
            decorated = cg(attrval, classname)
            classdict[attr] = decorated
            changed.append(decorated)
      ma = type.__new__(meta, classname, supers, classdict)
      return ma

class Stack:
  stack = ["main"]
  superstack = []
  @classmethod
  def isnotin(cls, l, ll):
     indices = [i for i, x in enumerate(ll) if x == l[0]]
     return not any([l == ll[i:len(l)] for i in indices])
  @classmethod
  def push(cls, e): cls.stack.append(e)
  @classmethod
  def pop(cls): return cls.stack.pop()
  @classmethod
  def superpush(cls):
    if all([cls.isnotin(cls.stack, ll) for ll in cls.superstack]):
       cls.superstack.append(cls.stack[:])

class cg:
  def __init__(self, func, clazz):
    self.func = func
    self.clazz = clazz
  def __call__(self, *args):
    Stack.push("\"{}.{}({})\"".format(self.clazz,self.func.__name__, *args))
    tmp = self.func(*args)
    Stack.superpush()
    Stack.pop()
    if (len(Stack.stack)==1):
        with open('cg.dot', 'w', encoding='utf-8') as out:
           out.write(self.graph(Stack.superstack))
    return tmp
  def graph(self, l):
    res = "strict digraph cg {\n"
    for t in l:
      res += "   "+" -> ".join(t)+"\n"
    return res + "}\n"

import ABC

A = ABC.A = CG('A', (), dict(ABC.A.__dict__))
B = ABC.B = CG('B', (), dict(ABC.B.__dict__))
C = ABC.C = CG('C', (), dict(ABC.C.__dict__))
