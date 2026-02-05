def f(x,y):
 if x>0:
  if y>0:
   return x+y
  else:
   return x-y
 else:
  if y>0:
   return y-x
  else:
   return -(x+y)
def g(l):
 r=[]
 for i in range(len(l)):
  if l[i]not in r:
   r.append(l[i])
 return r
def h(s):
 c=0
 for i in s:
  if i in'aeiouAEIOU':
   c=c+1
 return c
if __name__=='__main__':
 print(f(3,4))
 print(f(-3,4))
 print(f(3,-4))
 print(f(-3,-4))
 print(g([1,2,2,3,3,3]))
 print(h("hello world"))
