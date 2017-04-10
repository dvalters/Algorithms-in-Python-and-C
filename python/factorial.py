
def factoral(n):
  """Takes a number n, and calculates it's factorial using recursion"""
  if n < 0:
    return 0
  elif n == 0 or n == 1:
    return 1
  else:
    return n * factorial(n - 1)


  
