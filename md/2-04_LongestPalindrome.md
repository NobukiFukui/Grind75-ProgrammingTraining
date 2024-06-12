# 2-04_LongestPalindrome
Author: WaveAlchemist
URL: https://leetcode.com/problems/longest-palindrome/
Given a string s which consists of lowercase or uppercase letters, return the length of the longest 
palindrome
 that can be built with those letters.

Letters are case sensitive, for example, "Aa" is not considered a palindrome.

# 1st-2nd
20分ほど考えてみたもののアルゴリズムを構築することができなかった．
（頭の中では奇数個の文字を文字列の真ん中に配列して偶数個の文字を左右均等に振り分けるという手法が思い浮かんだ）

以下は回答例を見て実装したコード
https://leetcode.com/problems/longest-palindrome/solutions/5255201/easy-solution-simple-approach-c-python-java/

- 文字は1種類につき偶数個使える
- 1文字は１回のみ出現可能


偶数個の文字の種類だけ+1, 奇数個の文字の種類だけ-1を行う

``` Python
class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = 0 # odd
        freq = defaultdict(int)
        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1 # frequency of characteres
            if freq[ch] % 2 == 0:
                count -= 1
            else:
                count += 1
        if count > 1:
            return len(s) - count + 1
        return len(s)


```