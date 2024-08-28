def add(a,b):
  return (a+b)/2

res = add(10,20)
print(res)

def facto(x):
    if x == 0 or x == 1:
        return 1
    else:
        return x * facto(x-1)

