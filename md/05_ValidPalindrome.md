# 05_ValidPalindrome
Author: WaveAlchemist  
URL: https://leetcode.com/problems/valid-palindrome/

# 1st
方針：
アルファベットをすべて小文字にした後
文字列sの各要素を参照，対になるアフィリエイトが同じであればOK
そうでないならFalseを返す
最終的にループを抜けることができればTrueを返す
結果：
失敗
:等の記号を削除できていない

```Python
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_lower = s.lower()
        len_s = len(s)
        for i in range(int(len_s/2)):
            if s_lower[i] != s_lower[-i-1]:
                return False
        return True
```

# 2nd
方針：
filter関数を用いてアルファベット以外を削除する
結果：
成功

``` Python
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_filtered = filter(str.isalnum, s)
        s = "".join(s_filtered)
        s_lower = s.lower()
        len_s = len(s)
        for i in range(int(len_s/2)):
            if s_lower[i] != s_lower[-i-1]:
                return False
        return True
```