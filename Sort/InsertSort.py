
import random

"""
# 插入排序：
# 思路就是打扑克时，一边抓牌一边理牌的做法，
# 从第二个元素开始，查看是否比前面元素小，是的话，将前面大的元素依次往后挪，自己插入该空位
# 需要一个辅助空间
# 平均移动和比较次数为 n方/4，比冒泡和选择要再好一丢丢
"""


def InsertSort(nums):
    # 从第二个元素开始
    for i in range(1, len(nums)):
        tmp = nums[i]
        j = i - 1
        while j >= 0 and tmp < nums[j]:
            # 大的元素依次往后挪
            nums[j+1] = nums[j]
            # 别完了 往前移动 j 指针
            j -= 1
        nums[j+1] = tmp
    return nums


# 测试数据
def start():
    nums = [x*10 for x in range(1,11)]
    random.shuffle(nums)
    print(nums)

    print("===========排序后=================")
    nums = InsertSort(nums)
    print(nums)

if __name__ == '__main__':
    start()