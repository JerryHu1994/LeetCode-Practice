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
        self.food = []
        for f in food:  self.food.append((f[0], f[1]))
        self.snake = [(0, 0)] # tail - body - head
        self.score = 0

    def move(self, direction):
        """
        Moves the snake.
        @param direction - 'U' = Up, 'L' = Left, 'R' = Right, 'D' = Down 
        @return The game's score after the move. Return -1 if game over. 
        Game over when snake crosses the screen boundary or bites its body.
        :type direction: str
        :rtype: int
        """
        dirs = {'U': (0, -1), 'L': (-1, 0), 'R': (1, 0), 'D' : (0, 1)}
        dirx, diry = dirs[direction]
        heady, headx = self.snake[-1] # get the head
        nextx, nexty = headx+dirx, heady+diry
        if nextx < 0 or nextx >= self.width or nexty < 0 or nexty >= self.height or (nexty, nextx) in self.snake[1:]:   return -1
        if len(self.food) == 0: 
            self.snake.pop(0)
        elif (nexty, nextx) == self.food[0]:
            self.score += 1
            self.food.pop(0)
        else:
            self.snake.pop(0) # pop out the tail
        self.snake.append((nexty, nextx))
        return self.score

# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)