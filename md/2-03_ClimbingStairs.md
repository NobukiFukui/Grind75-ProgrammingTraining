# 2-03_ClimbingStairs
Author: WaveAlchemist
URL: https://leetcode.com/problems/climbing-stairs/description/
Description:
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

# 1st
- 方針：n段昇る方法がa(n)通りあるとすると，1段下からは1段の1通り，2段下からは1 or 2段の2通りで登ってくると考えられるのでa(n) = a(n-2) + a(n-1)通りとなる．コード上ではn-2段る登る方法をways_twolower，n-1段登る方法をways_onelowerとして，n段登るまでこれらを更新した
- 詰まった点：大学入試で経験したような問題で解法は思いつくもののコードに落とし込むのに30分以上かかった
- コードの意図：n<=2までは段数に等しい，それ以降は登った段数をiとしてn段登るまで（i<=n），n段登るときの方法ways_topにways_twolower, ways_onelowerを追加し更新する

``` Python
class Solution:
    def climbStairs(self, n: int) -> int:
        # n = 1 or 2
        if n <= 2: 
            return n
        # n >= 3 -> a_n = a_{n-2} + a_{n-1}
        ways_twolower = 1
        ways_onelower = 2
        ways_top = 0
        i = 3
        while i <= n:
            ways_top = ways_onelower + ways_twolower
            ways_twolower = ways_onelower
            ways_onelower = ways_top
            i += 1
        return ways_top
```

# 2nd-3rd
discord内では関連するレビューがなかったので，以下の解答を参考に再構築
3rdでは1から何も見ずに構築し，所要時間およそ4分


https://leetcode.com/problems/climbing-stairs/solutions/3708750/4-method-s-beat-s-100-c-java-python-beginner-friendly/

- コードの意図：0, 1段登るのを1通りとして，2段め以降順番に登ってways_onelowerとways_topを更新する


``` Python
class Solution:
    def climbStairs(self, n: int) -> int:
        # n <= 1 (including 0 stair) -> a(n) = 1
        if n <= 1:
            return 1
        # n >= 2 -> a(n) = a(n-2) + a(n-1)
        ways_current = 1 # no. of ways to climb current stairs (a(n-1))
        ways_lower = 1   # no. of ways to climb lower stairs   (a(n-2))
        # main loop
        for i in range(2, n+1):
            tmp = ways_current          # memorize no. of ways to climb current stairs
            ways_current += ways_lower  # renew no. of ways to climb current stairs
            ways_lower = tmp            # renew no. of ways to climb lower stairs
        return ways_current
```

# 4th
頂いたレビューをもとに再構築(何も見ずに5分で構築)
- いわゆる動的計画法で、DPテーブル(List)を用意して、前の情報を元に各値を更新していく形でも書けると思います (Mike0121様)

``` Python
class Solution:
    def climbStairs(self, n: int) -> int:
        # make DP table (n = 0 and 1 already included)
        options = [1, 1]
        # n = 0 or 1 --> 1 (early return)
        if n <= 1:
            return options[n]
        # n >= 2 --> options[n] = options[n-1] + options[n-2]
        # initialize iteration pointer
        i = 2
        while i <= n:
            options.append( options[i-2] + options[i-1] )
            i += 1
        return options[n]
```
# 5th
whileループよりもforループのほうが見やすいと判断し，書き直し

```Python
class Solution:
    def climbStairs(self, n: int) -> int:
        # make DP table (n = 0 and 1 already included)
        options = [1, 1]
        # n = 0 or 1 --> 1 (early return)
        if n <= 1:
            return options[n]
        # n >= 2 --> options[n] = options[n-1] + options[n-2]
        for i in range(2, n+1):
            options.append( options[i-2] + options[i-1] )
        return options[n]
```

# 6th
小田さんのコメントをもとに修正


- Python は
a, b = a + b, a
みたいな代入ができますが、したほうがいいかは微妙ですねえ。
- 再帰で書く方法があるかと思います。

コードの意図：メモ用の辞書を作成して，既にa(n)を計算していればそれを返す．そうでなければ，再帰を用いて
a(n) = a(n-2) + a(n-1)を行う
備考：@lru_cacheがないと時間がかかりすぎてtime limitになってしまった．
https://docs.python.org/ja/3/library/functools.html

``` Python
class Solution:
    @lru_cache(None)
    def climbStairs(self, n: int) -> int:
        memo = {}
        if n in memo:
            return memo[n]
        if n <= 2:
            result = n
        else:
            result = self.climbStairs(n - 1) + self.climbStairs(n - 2) 
        return result     

```