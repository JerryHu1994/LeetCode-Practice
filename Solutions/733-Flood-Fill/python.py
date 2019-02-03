class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        start_pix = image[sr][sc]
        height, width = len(image), len(image[0])
        queue = [[sr,sc]]
        visited = [[False]*width for i in range(height)]
        while len(queue):
            curr_r, curr_c = queue.pop(0)
            image[curr_r][curr_c] = newColor
            visited[curr_r][curr_c] = True
            # up
            if curr_r - 1 >= 0:
                if image[curr_r-1][curr_c] == start_pix and not visited[curr_r-1][curr_c]:
                    queue.append([curr_r-1, curr_c])
            # right
            if curr_c + 1 < width:
                if image[curr_r][curr_c+1] == start_pix and not visited[curr_r][curr_c+1]:
                    queue.append([curr_r, curr_c+1])
            # down
            if curr_r + 1 < height:
                if image[curr_r+1][curr_c] == start_pix and not visited[curr_r+1][curr_c]:
                    queue.append([curr_r+1, curr_c])
            # left
            if curr_c-1 >= 0:
                if image[curr_r][curr_c-1] == start_pix and not visited[curr_r][curr_c-1]:
                    queue.append([curr_r, curr_c-1])
        return image