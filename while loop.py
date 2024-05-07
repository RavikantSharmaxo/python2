# while loop
list_1= ["aaple","Banana","graphe","orange","pear","cherry"]

is_on_off = True
count = 0
while is_on_off:
    if count < len(list_1):
        print(list_1[count])
        count+=1
    else:
        is_on_off = False

