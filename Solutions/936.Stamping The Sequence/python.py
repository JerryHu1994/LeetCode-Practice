class Solution(object):
    def movesToStamp(self, stamp, target):
        """
        :type stamp: str
        :type target: str
        :rtype: List[int]
        """
        ls, lt = len(stamp), len(target)
        queue = collections.deque()
        done, ret = [False]*lt, []
        A = []
        for i in xrange(lt-ls+1):
            # for each window, maintain made and todo
            made, todo = set(), set()
            for j, char in enumerate(stamp):
                a = target[i+j]
                if a == char:
                    made.add(i+j)
                else:
                    todo.add(i+j)
            A.append((made, todo))
            
            # reverse the stamp at i right away
            if not todo:
                ret.append(i)
                for j in xrange(i, i+len(stamp)):
                    if not done[j]:
                        # the character is ready to be turned into ?
                        queue.append(j)
                        done[j] = True
        while queue:
            i = queue.popleft()
            # for windows that may affect
            for j in range(max(0, i-ls+1), min(i, lt-ls)+1):
                if i in A[j][1]:
                    # remove from the todo
                    A[j][1].discard(i)
                    # if the window has no todos, it can be replaced
                    if not A[j][1]:
                        ret.append(j)
                        # enqueue all elements
                        for k in A[j][0]:
                            if not done[k]:
                                queue.append(k)
                                done[k] = True
        return ret[::-1] if all(done) else []