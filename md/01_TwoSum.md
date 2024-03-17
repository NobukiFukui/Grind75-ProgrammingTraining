# 01_TwoSum
Author: WaveAlchemist  
Description:  
Pick up indeces of list where sum of two elements is X  
URL: https://leetcode.com/problems/two-sum/


# 1st
方針：numsの各要素をi, jの2つの変数を用いてforループで参照し，2つの要素和を計算する
i != jの時のみnums[i] + nums[j] を計算してtargetと等しいか検討
等しい場合は[i, j]を戻り値とする

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        for i in range(len(nums)):
            print("i = ",i, nums[i])
            for j in range(len(nums)):
                if j != i:
                    sum_tmp = nums[i] + nums[j]
                    if sum_tmp == target:
                        return [ i, j ]

``` 
# 2nd
参照している要素より左側の要素は既に一度和を計算しているので，
jについてのforループはi+1からnumsの要素数で

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if j != i:
                    sum_tmp = nums[i] + nums[j]
                    if sum_tmp == target:
                        return [ i, j ]
```

# 3rd
sum_tmpに和を代入せずにif文で直接判定する

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if j != i:
                    if nums[i] + nums[j] == target:
                        return [ i, j ]
```

# 4th
ハッシュテーブル（辞書配列）を利用する
https://leetcode.com/problems/two-sum/solutions/3619262/3-method-s-c-java-python-beginner-friendly/

iについてのforループ内で
pair = target - nums[i]で対になる要素が何かを計算
numMapで空の辞書配列を作成し，nums[i]をキーにインデックスを値に与えていく
もし，pairに対応する値がnumMapにあればその値を採用し，
numMap[pair]とiを対にして戻り値とする

```python
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
            numMap = {}
            for i in range(len(nums)):
                pair = target - nums[i]
                if pair in numMap:
                     return [numMap[pair], i]
                numMap[nums[i]] = i
```
