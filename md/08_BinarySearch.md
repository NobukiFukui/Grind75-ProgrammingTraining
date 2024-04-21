# 07_BinarySearch
Author: WaveAlchemist  
URL:https://leetcode.com/problems/binary-search/

# 1st
方針：
リストのindexメソッドを利用することを考える
targetがnumsに無いときは-1に返すようif分岐
一番これがシンプルかなと思いました

``` Python
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if target in nums:
            return nums.index(target)
        else:
            return -1
```
# 2nd
方針：
小田さんからご提案頂いたbisectを用いて再構築

``` Python
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        import bisect
        if target in nums:
            return bisect.bisect_left(nums, target)
        return -1
```

# 3rd
https://github.com/python/cpython/blob/3.12/Lib/bisect.py
も読んでみて，２分探索のアルゴリズムを構築する

``` Python
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if target in nums:
            lo = 0
            hi = len(nums)
            while lo < hi:
                mid = (lo + hi) // 2
                if nums[mid] < target:
                    lo = mid + 1
                else:
                    hi = mid
            return lo
        return -1
```