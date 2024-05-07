# lambda is know as anonymous fuction

x =lambda a, b, c: a +b +c
print(x(1,2,3))

# while loops how it's works

list_1 = [1,2,3,4,5,6]

on_off = True
count = 0

while on_off:
    if(count< len(list_1)):
        print(list_1[count])
        count+=1
    else:
        on_off = False

# tuple what is tuple unchangeable list of element in variable
# it is collection which is ordered are unchangeable or immutable


list_2 = ("hello","world","heee")

print(list_2)
# changing tuple values from element
this_tuple = ("ravi","kant","sharma")
this_tuple  = list(this_tuple) # convert tuple into list
this_tuple[2] = "ghimre"
tuple(this_tuple)# then into tuple
print(this_tuple)

# add item in tuple
list(this_tuple)
this_tuple.append("sharma")
tuple(this_tuple)
print(this_tuple)