
def partition(li,left, right):
    tmp = li[left]
    while left < right:
        while left < right and li[right] >= tmp:
            right -= 1   # 从后往前数, 若后面的数小于我们设置的数, 则不调换(索引往前减一), 若小于则调换
        li[left] = li[right]
        while  left < right and li[left] <= tmp:
            left += 1  # 上面调换过后就从前开始数, 与上反循环
        li[right] = li[left]
    li[left] = tmp
    return left  # 得到中间的索引,并且数组已经做了简单的排序,接着后面继续循环分治排序



def quick_sort(li,left, right):
    if left < right:
        mid = partition(li, left, right)
        quick_sort(li, left, mid - 1)
        quick_sort(li, mid + 1, right)


    
li = [7, 5, 4, 6, 3, 8, 2, 9, 1]

quick_sort(li, 0, len(li)-1)
print(li)
