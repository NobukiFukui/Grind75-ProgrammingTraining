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


