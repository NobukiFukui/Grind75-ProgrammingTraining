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

# 3rd
頂いたコメントをもとにコードを再構築する
- 自然な発想としては、偶数個の文字は全部使って、奇数個の文字はあれば一個だけ使うといった感じだと思います。やっていることに対して、コードが複雑に感じました。(liquorice様)

方針：
1) 偶数個の文字は両サイドに半分ずつ配列させる
2) 奇数個の文字はn-1個だけ偶数個の文字と同様に配列させる
3) 真ん中に奇数個の文字を1個だけ配列させる
例：aaaaabbccdde　⇒　aaaa ⇒ baaaab　⇒　・・・
⇒ bcdaaeaadcb or bcdaaaaadcb

最終的に4分2秒で構築できました
``` Python
class Solution:
    def longestPalindrome(self, s: str) -> int:
        # default dict for counting characters
        char_count = defaultdict(int)
        # count characters
        for char in s:
            char_count[char] += 1
        # initialize counter for length of palindorome
        count = 0
        odd_found = False
        # consitute palidorome
        for char in char_count.keys():
            if char_count[char] % 2 == 0: # even number -> use all
                count += char_count[char]
            else: # odd number -> use all characters except one character
                count += char_count[char] - 1
                odd_found = True
        if odd_found:
            count += 1 # add one character at center for odd character
        return count
```

# 3rd
頂いたコメントをもとにコードを再構築する
- 自然な発想としては、偶数個の文字は全部使って、奇数個の文字はあれば一個だけ使うといった感じだと思います。やっていることに対して、コードが複雑に感じました。(liquorice様)

方針：
1) 偶数個の文字は両サイドに半分ずつ配列させる
2) 奇数個の文字はn-1個だけ偶数個の文字と同様に配列させる
3) 真ん中に奇数個の文字を1個だけ配列させる
例：aaaaabbccdde　⇒　aaaa ⇒ baaaab　⇒　・・・
⇒ bcdaaeaadcb or bcdaaaaadcb

最終的に4分2秒で構築できました
``` Python
class Solution:
    def longestPalindrome(self, s: str) -> int:
        # default dict for counting characters
        char_count = defaultdict(int)
        # count characters
        for char in s:
            char_count[char] += 1
        # initialize counter for length of palindorome
        count = 0
        odd_found = False
        # consitute palidorome
        for char in char_count.keys():
            if char_count[char] % 2 == 0: # even number -> use all
                count += char_count[char]
            else: # odd number -> use all characters except one character
                count += char_count[char] - 1
                odd_found = True
        if odd_found:
            count += 1 # add one character at center for odd character
        return count
```

# 4th
マイナー修正
- countはわかりにくいのでpalindrome_lengthに
- for char in char_count.keys()のkeysは要らない

```Python
class Solution:
    def longestPalindrome(self, s: str) -> int:
        # default dict for counting characters
        char_count = defaultdict(int)
        # count characters
        for char in s:
            char_count[char] += 1
        # initialize counter for length of palindrome
        palindrome_length = 0
        odd_found = False
        # constitute palindrome
        for char in char_count:
            if char_count[char] % 2 == 0: # even number -> use all
                palindrome_length += char_count[char]
            else: # odd number -> use all characters except one character
                palindrome_length += char_count[char] - 1
                odd_found = True
        if odd_found:
            palindrome_length += 1 # add one character at center for odd character
        return palindrome_length
```

