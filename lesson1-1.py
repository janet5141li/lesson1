a=[1,2,3,4];
b=a.copy();
c=list(a);
d=a[:];
b[0]='b'
c[0]='c'
d[0]='d'
print('a:',a)
print('b:',b)
print('c:',c)
print('d:',d)