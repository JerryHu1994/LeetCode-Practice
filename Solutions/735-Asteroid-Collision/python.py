class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        stack = []
        for a in asteroids:
            if a > 0:
                stack.append(a)
            else:
                if len(stack) == 0: 
                    stack.append(a)
                    continue
                notdone = False
                while len(stack):
                    notdone = False
                    if stack[-1] > 0:
                        if stack[-1] > -a:
                            break
                        elif stack[-1] == -a:
                            stack.pop()
                            break
                        else:
                            stack.pop()
                            notdone = True
                    else:
                        stack.append(a)
                        break
                if notdone: stack.append(a)
        return stack