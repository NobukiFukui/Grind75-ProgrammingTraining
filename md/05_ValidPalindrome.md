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

# 3rd
野田さんのコメントを参考に修正
・s_lower -> lower
・int(len_s/2) -> len_s // 2 (PEP8に注意)

``` Python
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_filtered = filter(str.isalnum, s)
        s = "".join(s_filtered)
        lower = s.lower()
        len_s = len(s)
        for i in range(len_s // 2):
            if lower[i] != lower[-i-1]:
                return False
        return True
```

# 4th
高速化できないかを検討
- lequoriceさんコメント
こちら空間計算量はどうなってると思いますか？減らせそうですか？
⇒パッと見では難しそう？？？　ひとまずforループを使わない手法を考えてみたが，なかなかうまくいかず
実行時間が速いサンプルを参考にした

``` Python
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_filtered = filter(str.isalnum, s)
        s = "".join(s_filtered)
        lower = s.lower()
        return lower == lower[::-1]
```
    