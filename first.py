import copy
List = [3,2,5,4]
a = copy.copy(List)
print("shallow copy",a)
List[1] = 8
print(List)