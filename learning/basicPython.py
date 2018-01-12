# variable
one = 1;
two = 2;
double = 2.66666;
print(one);

#booleans
true_boolean = True;
false_boolean =False;

#string
my_name = "Frank Wang";
print(my_name)
habit = "Python 是一门有趣的语言\n加油！"
print(habit);
print("The habit length is %d"%(len(habit)))

#while loop
num =1;
while num <=5 :
    print(num,end='');
    num += 1;

#for loop

for i in range(1, 11):print(i,end='');


#array

my_array = [1,2,3,"666",4,5]
print();
for iter in my_array:
    print(iter,end='\t')
print();
print(my_array[0])
print(my_array[3],end='\n')

#append
book_shelf = []
book_shelf.append("Hello");
book_shelf.append("2018")
print(book_shelf[0])
print(book_shelf[1])

#dictionary
my_dictionary = {
    "name":"Frank Wang",
    "age":"27",
    "gender":"male"
}
print("My name is %s" %(my_dictionary["name"]))

my_dictionary["Where"] = "Beijing"
print(my_dictionary)

for key in my_dictionary:
    print("%s--->%s"%(key,my_dictionary[key]))

for key,value in my_dictionary.items():
    print("%s--->%s"%(key,value))

# **  //
print("10**5:%d,15//4:%d"%(10**5,15//4))