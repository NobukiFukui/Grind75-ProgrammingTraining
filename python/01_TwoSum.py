# ===============================================================
# (program) 01_TwoSum
# WaveAlchemist
# Description: 
# Pick up indeces of list where sum of two elements is X
# URL: https://leetcode.com/problems/two-sum/
# 
# ===============================================================

# ----
# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

# Example 2:

# Input: nums = [3,2,4], target = 6
# Output: [1,2]

# Example 3:

# Input: nums = [3,3], target = 6
# Output: [0,1]

# %%

# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
        
#         # nums = [2,7,11,15], target = 9
#         for i in range(len(nums)):
#             print("i = ",i, nums[i])
#             for j in range(len(nums)):
#                 if j != i:
#                     sum_tmp = nums[i] + nums[j]
#                     if sum_tmp == target:
#                         return [ i, j ]

# %%
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
            numMap = {}
            for i in range(len(nums)):
                complement = target - nums[i]
                if complement in numMap:
                     return [numMap[complement], i]
                numMap[nums[i]] = i
        
nums = [2,7,11,15]
target = 9
Solution.twoSum([],nums,target)
# %%
