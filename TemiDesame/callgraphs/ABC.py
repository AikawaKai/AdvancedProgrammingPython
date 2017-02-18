class A:
  def a(i):
    if i > 7:
      A.a(i-1)
    else: B.b(i)
    C.c(i//2)

class B:
  def b(i): B.bb(i)
  def bb(i):
    C.c(i)
    C.cc(i)

class C:
  def c(i):
    if i <=2: B.b(i-1)
    else: C.cc(i*2)
  def cc(i): pass
