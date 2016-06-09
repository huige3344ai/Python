# _*_ coding:utf-8  _*_
L = ['Bart', 'Lisa', 'Adam']
print('========\'for\' Method:=======')
for name in L:
   print('Hello,',name)
print('========\'while\' Method:=======')
n = len(L)
index = 0
while index<=2:
   print('Hello,',L[index])
   index=index+1
print('========\'List\' operate:=======')
L.insert(index,'Jerry')
print('========\'List\' insert(index,\'Jerry\'):=======')
print('index is %d,it\'s values is %s'%(index ,L[index]))
print('========\'List\' pop(index-1):=======')
L.pop(index-1)
for name in L:
   print('Hello,',name)
print('========\'Tuple\' :=======')
T=('one','two',['red','green'])
for num in T:
   print('num is ',num)
print('========\'Tuple\' change :=======')
T[2][0]='blue'
print('========\'Tuple\' change :=======')
print('T[2][0] is ',T[2][0])