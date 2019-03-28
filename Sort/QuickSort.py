
import random

"""
# 快速排序：
# 两个步骤：
# 选取关键字，即以该关键字为标准，小的放左边，大的放右边
# 二分回归，对以关键字分区的左右两边列表进行分解

# 是交换排序的改进

"""

def QuickSort(nums, low, high):
    if left < right:
        pivot = Partition(nums, low, high)
        QuickSort(nums, low, )



# 测试数据
def start():
    nums = [x*10 for x in range(1,11)]
    random.shuffle(nums)
    print(nums)

    print("===========排序后=================")
    # nums = ShellSort(nums)
    nums = ShellSortPlus(nums)
    print(nums)

if __name__ == '__main__':
    start()






