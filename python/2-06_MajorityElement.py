
# %%
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # dictionary for counting numbers of each element
        nums_count = defaultdict(int)
        # count numbers contained in nums
        for num in nums:
            if not nums_count[num]:
                nums_count[num] = 0
            nums_count[num] += 1
            if nums_count[num] > (len(nums) // 2):
                return num

solution = Solution()
nums = [1,2,2,2,1]
print(solution.majorityElement(nums))
# %%
import timeit
from collections import defaultdict
from typing import List

class Solution1:
    def majorityElement(self, nums: List[int]) -> int:
        num_count = defaultdict(int)
        length_num = len(nums)
        for num in nums:
            num_count[num] += 1
            if num_count[num] > length_num // 2:
                return num

class Solution2:
    def majorityElement(self, nums: List[int]) -> int:
        num_count = defaultdict(int)
        for num in nums:
            num_count[num] += 1
            if num_count[num] > len(nums) // 2:
                return num

# テストデータを用意
test_data = [3, 2, 3, 1, 3, 4, 3, 3]

# 計測対象の関数を呼び出すラッパー関数を定義
def test_solution1():
    solution = Solution1()
    return solution.majorityElement(test_data)

def test_solution2():
    solution = Solution2()
    return solution.majorityElement(test_data)

# timeitを使用して実行時間を計測
time_solution1 = timeit.timeit(test_solution1, number=100000)
time_solution2 = timeit.timeit(test_solution2, number=100000)

print(f"Solution1 time: {time_solution1}")
print(f"Solution2 time: {time_solution2}")