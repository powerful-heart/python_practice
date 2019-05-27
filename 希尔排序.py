# !/usr/bin/env python
# -*- coding: utf-8 -*-


def shell_sort(li):
    gap = len(li) // 2
    while gap > 0:
        for i in range(gap, len(li)):
            tmp = li[i]
            j = i - gap
            while j >= 0 and tmp < li[j]:
                li[j + gap] = li[j]
                j -= gap
            li[j + gap] = tmp
        gap //= 2


li = [7, 5, 4, 6, 3, 8, 2, 9, 1]
shell_sort(li)
print(li)
