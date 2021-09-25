class A():
  def __init__(self):
    print('A')

  @staticmethod
  def foo():
    print('foo')


class B():
  def __init__(self):
    print('B')

  @staticmethod
  def bar():
    print('bar')


# a C osztály az A és a B osztály tulajdonságait is örökli
class C(A, B):
  def foobar(self):
    self.foo()
    self.bar()


c = C()
c.foobar()