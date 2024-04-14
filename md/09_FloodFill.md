# 09_FloodFill
Author: WaveAlchemist  
URL:https://leetcode.com/problems/flood-fill/description/

# 1st
再帰関数の利用を考え，
周囲のセルをcolorにするという操作を終わるまで繰り返すという方針
⇒失敗

``` Python
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if image[sr][sc] == color:
            return image
        else:
            if image[sr-1][sc] == image[sr][sc]:
                image[sr-1][sc] = color
                image = self.floodFill(image,sr-1,sc,color)
            if image[sr+1][sc] == image[sr][sc]:
                image[sr+1][sc] = color
                image = self.floodFill(image,sr+1,sc,color)
            if image[sr][sc-1] == image[sr][sc]:
                image[sr][sc-1] = color
                image = self.floodFill(image,sr,sc-1,color)
            if image[sr][sc+1] == image[sr][sc]:
                image[sr][sc+1] = color
                image = self.floodFill(image,sr,sc+1,color)
            image[sr][sc] = color
            return image
```

# 2nd
以下を参考にして，再構築
https://leetcode.com/problems/flood-fill/solutions/3024503/c-python-7ms-beats-93-96/

5分以内で構築できるようにしました

修正点：
cellの色を変えるタイミングをif分岐の中ではなく
分岐の前に変更する

``` Python
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        # memory original color at target cell
        color_org = image[sr][sc]
        # check if color at target cell is the same as color
        if color_org == color:
            return image
        # change color at target cell
        image[sr][sc] = color
        # change color at adjacent cells
        if sr > 0 and image[sr-1][sc] == color_org:
            self.floodFill(image, sr-1, sc, color)
        if sc > 0 and image[sr][sc-1] == color_org:
            self.floodFill(image, sr, sc-1, color)
        if sr < len(image)-1 and image[sr+1][sc] == color_org:
            self.floodFill(image, sr+1, sc, color)
        if sc < len(image[0])-1 and image[sr][sc+1] == color_org:
            self.floodFill(image, sr, sc+1, color)
        return image


```

# 3rd
小田さんのコメントをもとに修正
・再帰関数(recursiveFill)を別途定義
・範囲チェックの仕方でif文の書き方を修正，添え字の使い方・意図に注意
・再帰を呼ぶときにdirectionを示すリストを定義しておいて，for文を使って隣接するセルを参照した

``` Python
class Solution:
    def recursiveFill(self, pixel, sr, sc, color_org, color_new):
        # if sr and sc are out of range
        if sr < 0 or sc < 0 or sr >= len(pixel) or sc >= len(pixel[0]):
            return
        # check corresponding cell has the same color
        if pixel[sr][sc] != color_org:
            return
        # fill color
        pixel[sr][sc] = color_new
        # define direction vectors
        direction_rows = [0, 1, 0, -1]
        direction_cols = [1, 0, -1, 0]
        # call recursive functions at adjacent cells
        for i in range(4):
            self.recursiveFill(pixel, sr + direction_rows[i], sc + direction_cols[i], color_org, color_new)
                
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        # check if color at target cell is the same as color
        color_org = image[sr][sc]
        if color_org == color:
            return image
        # call recursive function
        self.recursiveFill(image, sr, sc, image[sr][sc], color)
        return image
        
```



# 4th 
stackを使った解法

```Python
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        # check if image is empty or not
        if not image:
            return
        # get number of rows and cols
        nrows, ncols = len(image), len(image[0])
        # check if color at target cell is the same as color
        color_org = image[sr][sc]
        if color_org == color:
            return image
        # generate stack of target row and col
        stack = [(sr, sc)]
        # repeat loop while stack has elements
        while stack:
            row, col = stack.pop()
            if 0 <= row < nrows and 0 <= col < ncols and image[row][col] == color_org:
                image[row][col] = color
                stack.extend([(row + drow, col + dcol) for drow, dcol in [(1, 0), (-1, 0), (0, 1), (0, -1)]])
        return image
        
```
