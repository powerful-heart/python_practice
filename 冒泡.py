def bubble_sort(li):
    for i in range(len(li)):
        for j in range(len(li) - i - 1):
            if li[j] > li[j + 1]:
                li[j], li[j + 1] = li[j + 1], li[j]


li = [8, 5, 4, 6, 3, 9, 7, 2, 1]
bubble_sort(li)
print(li)
