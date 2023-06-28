# 0x05-python-exceptions
### 0. Safe list printing
This is a Python project that covers the topic of exceptions. Exceptions are events that occur during the execution of a program that disrupt the normal flow of instructions.
https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2020/9/070710952984e4d126e114405cefe83af2271ce8.gif?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20230628%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230628T102021Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=ddd1d76c750eb70fffe402c62926c4ef93b34894d320a77bbc5cf6068b5e8d35
#### mandatory
Write a function that prints x elements of a list.

* my_list can contain any type (integer, string, etc.)
* All elements must be printed on the same line followed by a new line.
* x represents the number of elements to print
* x can be bigger than the length of my_list
* Returns the real number of elements printed
* You have to use try: / except:
* You are not allowed to import any module
* You are not allowed to use len()

### 1. Safe printing of an integers list
Write a function that prints an integer with "{:d}".format().

* Prototype: `def safe_print_integer(value):`
* value can be any type (integer, string, etc.)
* The integer should be printed followed by a new line
* Returns *True* if value has been correctly printed (it means the value is an integer)
* Otherwise, returns `False`
* You have to use `try: / except:`
* You have to use `"{:d}".format()` to print as integer
* You are not allowed to import any module
* You are not allowed to use `type()`

