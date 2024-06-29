
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
