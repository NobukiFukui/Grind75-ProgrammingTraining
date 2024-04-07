# ===============================================================
# (program) 07_BinarySearch
# WaveAlchemist
# Description: 
# Given the root of a binary tree, invert the tree, and return its root.
# URL: https://leetcode.com/problems/binary-search/
# ===============================================================

#%%
class Solution:
    def search(self, nums: list[int], target: int) -> int:
        if target in nums:
            return nums.index(target)
        else:
            return -1

target = 9
nums = [-1,0,3,5,9,12]
solution = Solution()
a = solution.search(nums, target)
print(a)
# %%
