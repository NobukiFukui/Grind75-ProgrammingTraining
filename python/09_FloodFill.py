# ===============================================================
# (program) 09_FloodFill
# WaveAlchemist
# Description: 
# An image is represented by an m x n integer grid image where image[i][j] represents the pixel value of the image.

# You are also given three integers sr, sc, and color. You should perform a flood fill on the image starting from the pixel image[sr][sc].

# To perform a flood fill, consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color), and so on. Replace the color of all of the aforementioned pixels with color.

# Return the modified image after performing the flood fill.
#
# URL: https://leetcode.com/problems/flood-fill/description/
# ===============================================================

# %%
class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
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

image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1
sc = 1
color = 2
solution = Solution()
solution.floodFill(image, sr, sc, color)
# %%
