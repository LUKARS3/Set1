n = int(input())
if n % 4 == 0:
  if n % 100 == 0 and  n % 400 != 0:
    print('Not')
  else:
    print('Leap')
