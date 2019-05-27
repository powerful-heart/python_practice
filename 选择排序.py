
def select_sort(li):
    for i in range(len(li)-1):
        min_loc = i
        for j in range(i+1,len(li)):
            if li[j] < li[min_loc]:
                min_loc = j

        if min_loc != i:
            li[i], li[min_loc] = li[min_loc], li[i]

li = [7, 5, 4, 6, 3, 8, 2, 9, 1]
select_sort(li)
print(li)
