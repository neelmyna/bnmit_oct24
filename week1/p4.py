import sys

def partition(my_list, low, high):
    j = low
    pivot = my_list[high] #last element is the reference element
    for i in range(low, high):
        if my_list[i] < pivot:
            my_list[i], my_list[j] = my_list[j], my_list[i]
            j += 1
    my_list[j], my_list[high] = my_list[high], my_list[j]
    return j

def quick_sort(my_list, low, high):
    if low < high:
        pivot_index = partition(my_list, low, high)
        quick_sort(my_list, low, pivot_index-1)
        quick_sort(my_list, pivot_index+1, high)

numbers = list()
print(type(sys.argv))

for i in range(1, len(sys.argv)):
    numbers.append(float(sys.argv[i]))

print(f'User given numbers are: ', numbers)
quick_sort(numbers, 0, len(numbers)-1)
print(f'Sorted list is: ', numbers)