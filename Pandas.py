import pandas as pd
list_1 = {
    "name":"ravikant",
    "age":22,
}

var = pd.Series(list_1,index = [1,2,3])
var_2 = pd.DataFrame(list_1)
print(var_2)
def helloworld ():
    return "hello world"