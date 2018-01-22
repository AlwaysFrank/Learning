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