#!/user/bin/python3
#-*-coding:UTF-8-*-

path = './testFileStream.txt'
#write something
f_name = open(path,'w')
print('write length: ',f_name.write('Hello python3!'))

#read all
f_name = open(path,'r')
print('read file: ',f_name.read())

#read one by one
f_name = open(path,'r')
c_str = f_name.read(1)
while c_str:
    print('read one char: ',c_str)
    c_str = f_name.read(1)

#fileinput
import fileinput
for line in fileinput.input(path):
    print('line is :' ,line)

#iterator
f_name = open(path)
for line in f_name:
    print('line is :',line)

#close the file stream
f_name.close()

#streamIO
from io import StringIO

io_val = StringIO()

io_val.write('Hello python3 \n~~line2\n~~line3')

print('write : ',io_val.getvalue())

io_val = StringIO('Hello python3 \n~~line2\n~~line3')
while True:
    io_line = io_val.readline()
    if io_line == '':
        break
    print('line :',io_line)

#pickle
import  pickle
d = dict(name ='xiao ming', stu_number = '111')
print(pickle.dumps(d))

f_name = open(path,'wb')
try:
    print('write text:', f_name.write(pickle.dumps(d)))
finally:
    f_name.close()

f_name = open(path,'rb')
try:
    print('load text:', pickle.load(f_name))
finally:
    f_name.close()

#dumps loads
import json
data = {'num':1002,'name':'xiao ming','age':'27'}

json_data = json.dumps(data)
print('Python data ',data)
print('JSON data: ',json_data)

data2 = json.loads(json_data)
print('data2[name]',data2['name'])