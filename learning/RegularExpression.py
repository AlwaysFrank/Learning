#!/usr/bin/pythoon3
#-*-coding:UTF-8-*-

#mail regular expression
import  re

print(re.match('hello','hello python!').span())
print(re.match('world','hello python!'))

line = 'Cats are smarter than dogs???'

matchObj = re.match(r'dog',line , re.M | re.I)

if matchObj:
    print('use match, the match string is ',matchObj.group())
else:
    print('No such string!!!!!!')

matchObj = re.search(r'dogs', line, re.M | re.I)

if matchObj:
    print('use serach, the match string is ',matchObj.group())
else:
    print('No match string !!!!!!!!')

print(re.match(r'^(\d+)(0*)$','102300').groups())
print(re.match(r'^(\d+?)(0*)$','102300').groups())


#re.I(re.IGNORECASE): 忽略大小写（括号内是完整写法，下同）
#M(MULTILINE): 多行模式，改变'^'和'$'的行为（参见上图）
#S(DOTALL): 点任意匹配模式，改变'.'的行为
#L(LOCALE): 使预定字符类 \w \W \b \B \s \S 取决于当前区域设定
#U(UNICODE): 使预定字符类 \w \W \b \B \s \S \d \D 取决于unicode定义的字符属性
#X(VERBOSE): 详细模式。这个模式下正则表达式可以是多行，忽略空白字符，并可以加入注释。以下两个正则表达式是等价的：