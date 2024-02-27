#  import array module

# define array with  type code
# 'b' -> signed integer
# 'B' -> unsigned integer
# 'u' -> unicdoe char
# 'h' ->  signed integer
# 'H' -> unsigned integer
# 'i' -> signed integer
# 'I' -> unsigned integer
# 'l' -> signed integer
# 'L' -> unsigned integer
# 'q' -> signed integer
# 'Q' -> unsigned integer
# 'f' -> floating point
# 'd' -> floating integer

# Array methods
# append
# count
# extend
# fromlist
# index 
# insert
# pop 
# remove
# reverse 
# tolist
# len
# sum 
# max
# min 
# sorted


from array import *
a1 = array('i',[1,2,3])
print(a1)
print(type(a1))
for x in a1:
    print(x)