# 2-11_ContainsDuplicate
Author: WaveAlchemist
URL:https://leetcode.com/problems/contains-duplicate/

Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

 

Example 1:

Input: nums = [1,2,3,1]
Output: true
Example 2:

Input: nums = [1,2,3,4]
Output: false
Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true

# 1st
初見で解きました．
169. Majority Element等を思い出してdefaultdictを用いる方法で実装
（所要時間2min51s）
各数字の数を数えてdefaultdictに格納し，その値が2以上ならduplicatedと判定

``` Python
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums_count = defaultdict(int)
        # count numbers of each number
        for num in nums:
            nums_count[num] += 1
            # check duplicated numbers
            if nums_count[num] >= 2:
                return True
        return False
```

# 2nd
ほかにもhashsetを用いて解く方法をチェックしました．
参考：https://github.com/erutako/leetcode/pull/5
1, 2いずれの手法も空間計算量はO(n)でしょうか．

``` Python
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums_seen = set()
        for num in nums:
            if num in nums_seen:
               return True
            nums_seen.add(num)
        return False
```

勉強のためBrute ForceとSortも書いてみました．
- Brute Force（実行したら時間切れになりましたので，まあ除外でしょう，計算量はO(n^2)）
``` Python
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        n = len(nums)
        for i in range(n - 1):
            for j in range(i + 1, n):
                if nums[i] == nums[j]:
                    return True
        return False
```

- Sort(計算量はO(nlog n))
``` Python
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # sort nums
        nums.sort()
        # check numbers in nums
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]: # check numbers at i and i-1 idx
                return True
        return False
```
