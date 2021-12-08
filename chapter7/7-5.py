list1 = [8, 19, 148, 4]
list2 = [9, 1, 33, 83]
ans_list = []

for i in list1:
    for j in list2:
        ans = i * j
        ans_list.append(ans)

print(ans_list)