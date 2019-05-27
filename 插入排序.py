
def insert_sort(li):
    for i in range(1, len(li)):  # 从第一位开始与之前进行比较
        tmp = li[i]  # 需要插入的值
        j = i-1  # 需要插入值前一个值的索引
        while j >= 0 and tmp < li[j]:  # 索引必须大于等于零(此时)插入值最小, 且插入值需小于前一个值
            li[j+1] = li[j]  # 用钱一个值覆盖后一个值
            j -= 1  # 继续往前循环
        li[j+1] = tmp  # 以上条件不满足时, 要么需插入值最小, 要么大于前一个值,都需插入该值之后

li = [7, 5, 4, 6, 3, 8, 2, 9, 1]
insert_sort(li)
print(li)
                
