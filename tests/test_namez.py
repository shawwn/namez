import namez
from namez import typez
import typing

def test_namez():
  assert namez.name(test_namez) == __name__+'/test_namez'
  assert namez.get(__name__+'/test_namez') == test_namez
  namez.set(__name__+'/foo', 42)
  assert namez.get(__name__+'/foo') == 42
  assert foo == 42
  namez.set('bar', 42)
  assert namez.get('bar') == 42

def test_typez():
  assert typez.verify_type(3, int)
  assert typez.verify_type([3], typing.List[int])
  assert typez.verify_type((3,), typing.Sequence[int])
  assert typez.verify_type([(3,)], typing.List[typing.Tuple[int]])
