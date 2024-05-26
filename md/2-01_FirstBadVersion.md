# 2-01_FirstBadVersion
Author: WaveAlchemist  
Description:  
You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which returns whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.
URL: https://leetcode.com/problems/first-bad-version/description/

# 1st
まずは先頭から順番にisBadVersionでbad versionかどうかを判定
(線形探索)

⇒ 予想通りsubmit時にnが大きいケースだとタイムアウト
``` Python
class Solution:
    def firstBadVersion(self, n: int) -> int:
        i = 0
        while not isBadVersion(i):
            i += 1
        return i
```

# 2nd 
続いて二分探索を試してみる

``` Python
class Solution:
    def firstBadVersion(self, n: int) -> int:
        left = 1
        right = n
        while left <= right:
            mid = int( left + (right - left) / 2 )
            if isBadVersion(mid):
                right = mid - 1 
            else:
                left = mid + 1
        return left
```

# 3rd
colorboxさんの解法及びbisect.pyを参考にコードを書き換えました．

参照
- https://github.com/python/cpython/blob/main/Lib/bisect.py
- https://github.com/colorbox/leetcode/pull/16/files#diff-3b2fc736f07a08a8c16e0970102960042087a24fa739905a290d76bb0dea8a54

``` Python
class Solution:
    def firstBadVersion(self, n: int) -> int:
        left = 1
        right = n
        while left < right:
            mid = int( left + (right - left) / 2 )
            if isBadVersion(mid):
                right = mid
            else:
                left = mid + 1
        return left
```

# 4th
レビューをもとに修正．また，制約条件などをコメントに追記．
1から10分以内に再構築できるようにしました．
- 整数の割り算は//が使えます。(liquorice様)

``` Python
class Solution:
    def firstBadVersion(self, n: int) -> int:
        left = 1 
        right = n 
        # left can be bad/good version / right must be bad version
        # the first bad version is b/w left and right, both side inclusive
        while left < right:
            mid = left + (right - left) // 2
            if isBadVersion(mid):
                right = mid    # current version is bad version
            else:
                left = mid + 1 # current version is good version -> mid + 1 should be checked
        return left
```