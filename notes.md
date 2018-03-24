# If Else
```python
weight = float(input("Please enter your weight: "))
height = float(input("Please enter your height: "))
bmi = weight/height/height

if bmi < 18.5:
    print("过轻！")
elif bmi >= 18.5 and bmi <= 25:
    print('正常!')
elif bmi > 25 and bmi < 28:
    print('过重!')
elif bmi >=28 and bmi <= 32:
    print('肥胖!')
elif bmi > 32:
    print('严重肥胖!')

```
# For, While
```python
L = ['Bart', 'Lisa', 'Adam']
n = 3
while n > 0:
    print('Hello, %s' % L[n-1])
    n = n - 1
```
# Dict
```python
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print(d['Bob'])
print('Bob' in d)
d.get('Bob')
d.get('Bob',100)
```
# Set
```python
s = set([1,1,2,3])
s1 = set(9)
s.add(4)
s.remove(2)
s1 & s2
s1 | s2
```
`set`,`str`是不可变对象，`list`是可变对象

# Function
## Define a function
* 空函数，什么事情也不做

```python
def nop():
    if age > 18:
        pass
```

* 函数返回值是返回tuple，在多函数返回时

```python
import math

def move(x,y,step,angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx,ny

x,y = move(100, 100, 60, math.pi / 6)
print(x,y)
r = move(100, 100, 60, math.pi /6)
print(r)
```

```python
delta = b*b - 4*a*c
if delta < 0:
    print('no solution')
elif delta == 0:
    ans = -b/2/a
    return ans,ans
else:
    ans1 = (-b+math.sqrt(delta))/(2*a)
    ans2 = (-b-math.sqrt(delta))/(2*a)
    return ans1,ans2
```

## [Parameter of the Function](https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001431752945034eb82ac80a3e64b9bb4929b16eeed1eb9000)
### 位置参数

```python
def power(x):
  return x * x

def power(x,n):
  s = 1
  while n > 0:
    n = n - 1
    s = s * x
  return s
```
### 默认参数

```python
def power(x,n=2):
  s = 1
  while n > 0:
    n = n - 1
    s = s * x
  return s
```
必选参数在前，默认参数在后
```python
def enroll(name, gender, age=6, city='Beijing'):
  print('name:',name)
  print('gender:',gender)
  print('age:',age)
  print('city:',city)
```
如果不按照顺序的话，要把默认参数显示表示
#### P.S. 默认参数的坑
```python
def add_end(L=[]):
  L.append('End')
  return L
print(add_end([1,2,3]))
print(add_end(['x','y','z']))
print(add_end())
print(add_end())
print(add_end())
```
**定义默认参数必须牢记一点：默认参数必须指向不变的对象**

### 可变参数

1. 不可变参数时

```python
def calc(numbers):
  sum = 0
  for n in numbers:
    sum = sum + n * n
  return sum
print(calc([1,2,3]))
```
2. 可变参数时

```python
def calc(*numbers):
  sum = 0
  for n in numbers:
    sum = sum + n * n
  return sum

print(calc(1,2,3))
  ```
本质上少打了一个方括号
#### P.S.
* 把`list`或者`tuple`变成可变参数传入：`calc(*numbers)`

### 关键字参数
可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个**tuple**。而关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个**dict**
```python
def person(name,age,**kw):
  print('name:',name,' age:',age,' other:',kw)

person('Michael',30)
person('Bob',35,city='Beijing')
person('Adam',45,gender='M',job='Engineer')
```
#### 命名关键字参数
```python
def person(name, age, *, city, job):
  print(name, age, city, job)

person('Jack', 24, city='Beijing', job='Engineer')

#会报错
person('Jack', 24, 'Beijing', 'Engineer')
```
#### 参数组合
```python
def f1(a, b, c=0, *args, **kw):
  print('a =', a,'b =', b,'c =', c,'args =', args, 'kw =', kw)

def f2(a, b, c=0, *, d, **kw):
  print('a =', a, 'b =', 'c =', c,'d =', d, 'kw =', kw)

f1(1, 2)
f1(1, 2, c=3)
f1(1, 2, 3, 'a', 'b')
f1(1, 2, 3, 'a', 'b', x=99)

f2(1, 2, d=99, ext=None)
```
### Homework
```python
def product(*numbers):
    n = len(numbers)
    if n == 0:
        raise TypeError()
    else:
        prod = 1
        for i in numbers:
            prod = prod * i
        return prod

# 测试
print('product(5) =', product(5))
print('product(5, 6) =', product(5, 6))
print('product(5, 6, 7) =', product(5, 6, 7))
print('product(5, 6, 7, 9) =', product(5, 6, 7, 9))
if product(5) != 5:
    print('测试失败!')
elif product(5, 6) != 30:
    print('测试失败!')
elif product(5, 6, 7) != 210:
    print('测试失败!')
elif product(5, 6, 7, 9) != 1890:
    print('测试失败!')
else:
    try:
        product()
        print('测试失败!')
    except TypeError:
        print('测试成功!')
```
## Recursive function
```python
def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)

print(fact(1))
print(fact(5))
print(fact(120))
```
### Homework
汉诺塔（没想太明白）
```python
def move(n, a, b, c):
    if n == 1:
        print(a, '-->', c)
    else:
        move(n-1, a, c, b)
        move(1, a, b, c)
        move(n-1, b, a, c)
move(3, 'A', 'B', 'C')
```
