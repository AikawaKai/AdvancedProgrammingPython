import re, string

from switch import *

class P(Switch):
  @case([x+y for x in string.ascii_lowercase for y in ['s', 'x', 'z']])
  def sxz_to_es(self, noun): return re.sub('$', 'es', noun)

  @case([x+'h' for x in string.ascii_lowercase if x not in 'aeioudgkprt'])
  def noisy_h(self, noun): return re.sub('$', 'es', noun)

  @case([x+'y' for x in string.ascii_lowercase if x not in 'aeiou'])
  def consonant_y(self, noun): return re.sub('y$', 'ies', noun)

  @case('default')
  def default(self, noun): return noun + 's'

  def plural(self, noun):
    return self.match(noun[-2:])(noun)

class N(Switch):
  @case(1)
  def january(self): return ("January")
  @case(2)
  def february(self): return ("February")
  @case(3)
  def march(self): return ("March")
  @case(4)
  def april(self): return ("April")
  @case(5)
  def may(self): return ("May")
  @case(6)
  def june(self): return ("June")
  @case(7)
  def july(self): return ("July")
  @case(8)
  def august(self): return ("August")
  @case(9)
  def september(self): return ("September")
  @case(10)
  def october(self): return ("October")
  @case(11)
  def november(self): return ("November")
  @case(12)
  def december(self): return ("December")
  def month(self, n): return self.match(n)()

class S(Switch):
  @case((12,1,2))
  def winter(self, n): return "{} comes in {}".format(N().month(n), "winter")

  @case((3,5,4))
  def spring(self, n): return "{} comes in {}".format(N().month(n), "spring")

  @case((6,7,8))
  def summer(self, n): return "{} comes in {}".format(N().month(n), "summer")

  @case('default')
  def fall(self, n): return "{} comes in {}".format(N().month(n), "fall")

  def season(self, n): return self.match(n)(n)

if __name__ == '__main__':
  p = P()
  print(p.plural('daily'))
  print(p.plural('cheetah'))
  print(p.plural('coach'))
  print(p.plural('fax'))
  print(p.plural('day'))

  s = S()
  print(s.season(7))
  print(s.season(1))
  print(s.season(10))
  print(s.season(4))
