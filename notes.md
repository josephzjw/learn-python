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
## Dict
```python
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print(d['Bob'])
print('Bob' in d)
d.get('Bob')
d.get('Bob',100)
```
## Set
```python
s = set([1,1,2,3])
s1 = set(9)
s.add(4)
s.remove(2)
s1 & s2
s1 | s2
```
`set`,`str`是不可变对象，`list`是可变对象 
