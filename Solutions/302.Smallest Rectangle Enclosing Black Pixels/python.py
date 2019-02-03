class Solution(object):
    def minArea(self, image, x, y):
        """
        :type image: List[List[str]]
        :type x: int
        :type y: int
        :rtype: int
        """
        height, width = len(image), len(image[0])
        left, right, top, bottom = float("inf"), float("-inf"), float("inf"), float("-inf")
        queue, visited = [(y,x)], set([(y,x)])
        while len(queue):
            currx, curry = queue.pop(0)
            left, right, top, bottom = min(currx, left), max(right, currx), min(top, curry), max(bottom, curry)
            if currx > 0 and (currx-1, curry) not in visited and image[curry][currx-1] == "1":
                queue.append((currx-1, curry))
                visited.add((currx-1, curry))
            if currx < width-1 and (currx+1, curry) not in visited and image[curry][currx+1] == "1":
                queue.append((currx+1, curry))
                visited.add((currx+1, curry))
            if curry > 0 and (currx, curry-1) not in visited and image[curry-1][currx] == "1":
                queue.append((currx, curry-1))
                visited.add((currx, curry-1))
            if curry < height-1 and (currx, curry+1) not in visited and image[curry+1][currx] == "1":
                queue.append((currx, curry+1))
                visited.add((currx, curry+1))
        return (right-left+1)*(bottom-top+1)