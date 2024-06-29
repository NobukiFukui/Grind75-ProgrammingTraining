# 2-06 MajorityElement
Author: WaveAlchemist
URL: https://leetcode.com/problems/majority-element/description/

Given an array nums of size n, return the majority element.
The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.
Example 1:
Input: nums = [3,2,3]
Output: 3

Example 2:
Input: nums = [2,2,1,1,1,2,2]
Output: 2

# 1st 
defaultdict nums_countを用いて，各要素の個数をカウント
各要素の個数が過半数を超えた時点でその要素を返す
所要時間 4min46s
実行時間 172ms

``` Python
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
```

# 2nd
discord上のほかの議論を参照
・Boyer-Moore majority vote algorithm
要素が同じであればcountに+1をし，そうでなければ-1を行う
要素が過半数ない場合はcountが0をまたぐので，その時点で候補を変更する
https://leetcode.com/problems/majority-element/solutions/3676530/3-method-s-beats-100-c-java-python-beginner-friendly/

``` Python
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        majority_candidate = 0
        for num in nums:
            if count == 0:
                majority_candidate = num
            if num == majority_candidate:
                count += 1
            else:
                count -= 1
        return majority_candidate
```

# 3rd
・kitakenさんのご指摘
defaultdictの場合はこの場合分け不要

``` Python
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        num_count = defaultdict(int)
        for num in nums:
            num_count[num] += 1
            if num_count[num] > len(nums) // 2:
                return num
```
# 4th
・kouさんのコメント
こちら len（）がどのくらいコスト掛かるかはみておいても良いと思いました。
ループの中で使うより先に定義して置く方が良いと思います
⇒
timeitを用いて調べると以下のように実行時間に差が出現．
事前定義をする場合 time: 0.7654874669999856
事前定義をしない場合 time: 0.9718373919999976

``` Python
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums_count = defaultdict(int)
        nums_length = len(nums)
        for num in nums:
            nums_count[num] += 1
            if nums_count[num] > nums_length // 2:
                return num
```

