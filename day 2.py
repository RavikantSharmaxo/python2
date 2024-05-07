# reverse all item in list
list_1 = [100,200,300,400,500]
new_list = []
count = len(list_1)-1
for i in list_1:
    new_list.append(list_1[count])
    count-=1
print(new_list)
# concadenate two index index-wise
list_1 = ["m","na", "i","ra"]
list_2 = ["y","me","s","vi"]
new_list = []
count = 0
for i in list_1:
    new = list_1[count]+list_2[count]
    new_list.append(new)
    count+=1
print(new_list)
#turn every item in list into square
list_1 = [1,2,3,4,5]
new_list = []
for i in list_1:
    new_list.append(i*i)
print(new_list)
# concadenate two list index with space
list_1 = ["hello","bye"]
list_2 = ["world","bye"]
new_list = []
count = 0
for i in list_1:
    new = i + " " +list_2[count]
    new_list.append(new)
    count+=1
print(new_list)

class artist:
    def __init__(self,name,stream,gender):
        self.name = name
        self.stream = stream
        self.gender = gender
class rnb(artist):
    def __init__(self,name,stream,gender,genre):
        artist.__init__(self,name,stream,gender)
        self.genre = genre
rn = rnb("the weeknd","50 billion","male","RNB")
print(rn.genre)
import random
num = random.randint(0,2)
list_question = ["what is your name ","what is your age ","what is your quest "]
answer = input(list_question[num])
print(answer)