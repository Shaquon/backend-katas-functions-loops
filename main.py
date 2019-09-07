def add(x,y):
  return x+y

def multiply(x,y):
  up=0
  for i in range(0,1):
    up=add(up,y)
  return up

def power(x,n):
 top = 1
 for i in range(1,n):
  multiply(top,x)
  return

def factorial(x):
  tree = x
  for i in range(2,x):
    tree=multiply(tree,x-1)
  return tree

def fibonacci(n):
  bus=0
  lego = 0
  bat =1
  if n == 0:
    return "Error"
  elif n == 1:
    return 0
  elif n == 2:
    return 1
  else:
    for k in range(0,n):
      bus = add(lego, bat);
      lego = bat
      bat = bus
  return bus