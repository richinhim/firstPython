f="x= %0.5f, y= %5.2f" %(1.234567, 9.87654321)
print(f)
print()
print("="*100)

i = 123
f=1.14159
s='python'
s1="python-1"
print("i=%d, f=%f, s=%s, s1=%s1" %(i,f,s,s1))

print()
print("="*100)

#dictionary
p={'name':'HanSaLam', 'age':28}
print("name=%(name)s age=%(age)d" %p)

print()
print("="*100)

print("i={0} f={1} s={2} s1={3}".format(123, 1.14159,12345, 'python', 'python-1'))

print()

#int, float, bool, None: 파이썬의 자료형
x=100
y=200
print(x+y)

x="100"
y="200"
print(x+y)

print(int(7.5))

print(2e5)

print(float("1.6"))



print(bool(0))

print(bool(-1))

print(bool("false"))

a=None
print(a is None)

print(0b1010)

print(type(123))

print(7/4)

print(7//4)


