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

