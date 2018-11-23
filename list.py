#!/usr/bin/env python
list = [5,3,7,4,2,4,3,57,3,75,5,732,4]
new_list = []
for i in list:
    if i<=5:
        new_list.append(i)
        new_list.sort(key=int, reverse=True)
print(new_list)
