from random import randint

def generator(n, max_value = 100):
    ls = []
    for i in range(n):
        ls.append(randint(0,max_value))
    return ls

def remove_even_zeroes(ls):
    index = 0
    zero_count = 0
    while index <= len(ls) - 1:
        if ls[index] == 0:
            zero_count += 1
            if zero_count % 2 == 0 and zero_count != 0:
                ls.pop(index)
                index -= 1
        index += 1
    return ls

def bubble_sort(ls):
    all_sorted = False
    while not all_sorted:
        all_sorted = True
        for i in range(len(ls) - 1):
            if ls[i] > ls[i + 1]:
                temp1 = ls[i]
                ls[i] = ls[i + 1]
                ls[i + 1] = temp1
                all_sorted = False
    return ls

def insert_sort(ls):
    for i in range(len(ls)):
        j = i
        while i > 0 and ls[j - 1] > ls[i]:
            j -= 1
            continue
        ls.insert(j, ls.pop(i))
    return ls

def quicksort(ls):
    if len(ls) <= 1:
        return ls
    pivot = ls[0]
    ls.pop(0)
    higher = []
    lower = []
    for item in ls:
        if item <= pivot:
            lower.append(item)
            continue
        higher.append(item)
    return quicksort(lower) + [pivot] + quicksort(higher)

gen = [0, 3, 1, 0, 5, 2, 0, 4, 2, 2, 0, 0, 3, 1, 5, 4, 4, 3, 2, 0] #generator(20, 5)
print(gen)
#print(bubble_sort(gen))
#print(insert_sort(gen))
#print(quicksort(gen))