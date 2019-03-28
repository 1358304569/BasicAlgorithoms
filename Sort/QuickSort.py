
import random
import sys


# 解决RecursionError: maximum recursion depth exceeded in comparison
sys.setrecursionlimit(100000)  # 例如这里设置为一百万

"""
# 快速排序：
# 两个步骤：
# 选取关键字，即以该关键字为标准，小的放左边，大的放右边
# 二分回归，对以关键字分区的左右两边列表进行分解

# 是交换排序的改进

"""


def Partition(nums, low, high):
    """
    @brief 求关键字，返回其角标
    """
    # 取第一个值为关键字
    pivotValue = nums[low]
    while low < high:
        # 比关键字大的，就放在右边
        while low < high and pivotValue < nums[high]:
            high -= 1
        # 碰到比关键字小的，交换至关键字的左边
        # 因为本程序中设置的pivot是low角标的值，所以直接将low 和 high交换
        nums[low], nums[high] = nums[high], nums[low]

        # 比关键字小的， 就保持放在左边
        while low < high and pivotValue > nums[low]:
            low += 1
        nums[low], nums[high] = nums[high], nums[low]

    # 到最后，low = high ，此时指向的角标即为pivot
    return low



def QuickSort(nums, low, high):
    """
    @brief 递归分解
    """
    if low < high:
        pivot = Partition(nums, low, high)
        QuickSort(nums, low, pivot)
        QuickSort(nums, pivot + 1, high)
    return nums



# 测试数据
def start():
    nums = [x*10 for x in range(1,11)]
    random.shuffle(nums)
    print(nums)

    print("===========排序后=================")
    low = 0
    high = len(nums) - 1
    nums = QuickSort(nums, low, high)
    print(nums)

if __name__ == '__main__':
    start()






