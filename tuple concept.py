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

this_tuple = ("apple") # this is not tuple
this_tuple = ("apple",) # this is tuple within single item there must comma in last
# unpacking in tuple

complete_name = ("ravi","kant","sharma")
(first,middle,last) = complete_name # this is called unpacking
print(first)
print(middle)
print(last)
complete_name = ("ravi", "kant", "sharma", "ghimire")
(first, middle, *last) = complete_name # using * we can assign last variable with remaining tuplr
print(first)
print(middle)
print(last)

list  =  ["hello","world"]
[hello,world] = list
print(hello)
print(world)