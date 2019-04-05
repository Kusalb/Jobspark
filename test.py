import re
li = ["raman           \n " , "Sid \n                   ", "\n saura ", "  "]
list1 = []
for i in li:
    j = re.sub(r"\s+", "", i)
    list1.append(j)

print(list1)

list2 = [x for x in list1 if x ]
print(list2)