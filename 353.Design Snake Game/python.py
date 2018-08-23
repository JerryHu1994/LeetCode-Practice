class SnakeGame(object):

    def __init__(self, width, height, food):
        """
        Initialize your data structure here.
        @param width - screen width
        @param height - screen height 
        @param food - A list of food positions
        E.g food = [[1,1], [1,0]] means the first food is positioned at [1,1], the second is at [1,0].
        :type width: int
        :type height: int
        :type food: List[List[int]]
        """
        self.width = width
        self.height = height
        self.foodlist = food
        self.snakelist = [[0, 0]]
        self.foodcnt = 0

    def move(self, direction):
        """
        Moves the snake.
        @param direction - 'U' = Up, 'L' = Left, 'R' = Right, 'D' = Down 
        @return The game's score after the move. Return -1 if game over. 
        Game over when snake crosses the screen boundary or bites its body.
        :type direction: str
        :rtype: int
        """
        head = self.snakelist[0][:]
        if direction == "U":
            head[0] -= 1
        elif direction == "L":
            head[1] -= 1
        elif direction == "R":
            head[1] += 1
        else:
            head[0] += 1
        # check if it is out of bound
        if head[0] < 0 or head[0] >= self.height or head[1] < 0 or head[1] >= self.width:
            return -1
        
        # check if the next one is the food
        if len(self.foodlist) > 0 and head == self.foodlist[0]:
            self.foodlist = self.foodlist[1:]
            self.foodcnt += 1
            self.snakelist.insert(0, head)
            return self.foodcnt
        else:
            # check if the snake bites itself
            body = self.snakelist[:-1]
            if head in body:
                return -1
            self.snakelist = [head] + body
        
        return self.foodcnt

# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)