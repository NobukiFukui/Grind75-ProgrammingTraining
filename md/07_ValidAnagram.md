# 07_ValidAnagram
Author: WaveAlchemist  
URL: https://leetcode.com/problems/valid-anagram/description/

# 1st 
方針：
s, tをリストに変換し，アルファベット順に並び替える
slistとtlistの各要素を比較し，等しければTrue，そうでなければFalseを返す
``` Python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        slist = sorted(list(s))
        tlist = sorted(list(t))
        for sl, tl in zip(slist, tlist):
            if sl != tl:
                return False
        return True
```

# 2nd 
リストでなくとも，sorted関数は使えるので修正
``` Python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        slist = sorted(s)
        tlist = sorted(t)
        for sl, tl in zip(slist, tlist):
            if sl != tl:
                return False
        return True
```

# 3rd
Runtimeの高速化を図るため，早いコードを参考．
sをセットに変換して，各文字の個数をs, tについて計上
個数が等しければTrueを返す

``` Python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        sSet = set(s)
        for ch in sSet:
            if s.count(ch) != t.count(ch):
                return False
        return True
```

# 4th
kitakenさんのコードも参考によりシンプルに書いてみました．
https://github.com/Kitaken0107/GrindEasy/pull/10#pullrequestreview-1956804905
``` Python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
```

# 5th
countを知らない想定で書いてみる
⇒ defaultdictを使った解法

参照
- https://docs.python.org/ja/3/library/collections.html#collections.defaultdict

```Python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # check if length of each string
        if len(s) != len(t):
            return False
        # make default dictionary for counting
        char_count = defaultdict(int)
        # count number of each alphabet
        for char in s:
            char_count[char] += 1
        # check if number of each alphabet in string t
        for char in t:
            if char_count[char] == 0: # t does not have char included in s
                return False
            char_count[char] -= 1
        return True
```