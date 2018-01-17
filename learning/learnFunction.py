#!/user/bin/python3
#-*-coding:UTF-8-*-

# * can save some untitled variable    ** for some key word variable
def my_function(para1, para2, para3, *vart,**kw):
    print('para1=', para1,'para2=', para2,'para3=', para3,'vart=',vart,'kw = ',kw)
    return

args = (1,2,3,4)                        #tuple
kw = {'name':'Frank','age':27}        #dict

my_function(*args, **kw)

#return as a function
def sum_late(*args):
    def calc_sum():
        num = 0
        for i in args:
            num = num + i
        return num
    return calc_sum

calc = sum_late(1,2,3,4)
print('result : ',calc())

#closure
def count_function():
    fs = []
    for i in range(1,4):
        def f():
            return i * i
        fs.append(f())  # notice f() as a result
    return fs

f1, f2, f3 = count_function()
print(f1, f2, f3)# 1 4 9

def count_function():
    fs = []
    for i in range(1,4):
        def f():
            return i * i
        fs.append(f) # notice f as a function
    return fs

f1, f2, f3 = count_function()
print(f1(),f2(),f3()) # 9 9 9

# recursion

def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)

print('fact(5):',fact(5))

def fact_iter(number, product):
    if number == 1:
        return product
    return fact_iter(number - 1, number * product)

print('fact_iter(5):',fact_iter(5,1))

# partial function,   use first parameter as pritial fumction's first parameter
from functools import partial
def mod (n, m):
    return n % m

mod_by_100 = partial(mod, 100)

print('100 % 7 = ',mod(100, 7))
print('100 % 7 = ',mod_by_100(7))