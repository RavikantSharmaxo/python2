class person:
    def __init__(self,name,age,hobbies):
        self.name = name
        self.age = age
        self.hobbies = hobbies
person_define = ["name","age","hobbies"]
collect = []
for  i in person_define:
    ques = input("what is your "+i+ " ")
    collect.append(ques)

p1 = person(collect[0],collect[1],collect[2])
print(p1.name)
print(p1.age)
print(p1.hobbies)

class students(person): # this is called inheritance i pass all quality of person students is child class person is parent class
    pass

class employee:
    salary_raise = 1.11
    def __init__(self,name,salary,age):
        self.name = name
        self.age = age
        self.salary = salary
    def rasing_salary(self):
        print("So your slary will raise by " +str(self.salary*self.salary_raise))
class developer(employee):
    salary_raise = 1.12
    def __init(self,name,age,salary,work):
        super().__init__(name,age,salary)
        self.work =work
class manager(developer):
    salary_raise = 1.13
    def __init(self,name,age,salary,work,emp = None):
        super().__init__(name,age,salary,work)
    def addemp(self,emp):
        if emp is None:
            self.emp =emp
        