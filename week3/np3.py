def read_heights(section):
    m = int(input(f'Enter number of girls of section-{section}: '))
    heights = []
    print(f'Enter {m} heights of girls of Section-{section}: ')
    for i in range(m):
        heights.append(int(input()))
    return heights

list1 = read_heights('A')
list2 = read_heights('B')

list1.sort()
list2.sort()
merged_list = list()

j = 0
i = 0
while i < len(list1) and j < len(list2):
    if list1[i] < list2[j]:
        merged_list.append(list1[i])
        i += 1
    else:
        merged_list.append(list2[j])
        j += 1
merged_list.extend(list1[i:])
merged_list.extend(list2[j:])

print(merged_list)
