
import random

"""
# 选择排序：
# 
# 在前面冒泡排序时，选出一个最值有可能要经过 n 比较和 n-1 次交换
# 其实只要【比较 n 次，选出最值，然后交换一次】就行了，
# 时间复杂度虽然和冒泡一样是 n2，但是交换次数少了，相对来说还是要好上一丢丢。

"""

def SeletSort(nums):
    for i in range(len(nums)-1):
        # 记录最小值角标
        target = i
        # 对后续的元素寻找最小值的角标
        for j in range(i+1, len(nums)):
            if nums[j] < nums[target]:
                target = j

        # 不等，说明找到最小值，交换
        if target != i:
            nums[i], nums[target], = nums[target], nums[i]
    return nums


# 测试数据
def start():
    nums = [x*10 for x in range(1,11)]
    random.shuffle(nums)
    print(nums)

    print("===========排序后=================")
    nums = SeletSort(nums)

    print(nums)

if __name__ == '__main__':
    start()
