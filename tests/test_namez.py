import namez

def test_namez():
  assert namez.name(test_namez) == __name__+'/test_namez'
  assert namez.get(__name__+'/test_namez') == test_namez
  namez.set(__name__+'/foo', 42)
  assert namez.get(__name__+'/foo') == 42
  assert foo == 42
  namez.set('bar', 42)
  assert namez.get('bar') == 42
