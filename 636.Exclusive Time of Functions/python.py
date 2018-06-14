class Solution(object):
    def exclusiveTime(self, n, logs):
        """
        :type n: int
        :type logs: List[str]
        :rtype: List[int]
        """
        stack = []
        ret = [0]*n
        interval = 0
        stamp_id, start_or_end, time = logs[0].split(":")
        stack.append(int(stamp_id))
        prev = int(time)
        for i in range(1,len(logs)):
            stamp_id, start_or_end, time = logs[i].split(":")
            stamp_id, time = int(stamp_id), int(time)
            if len(stack) == 0:
                stack.append(stamp_id)
                prev = time
            else:
                if start_or_end == "start":
                    lastid = stack[-1]
                    ret[lastid] += time - prev
                    stack.append(stamp_id)
                    prev = time
                else:
                    lastid = stack.pop()
                    ret[lastid] += time - prev + 1
                    prev = time + 1
                
        return ret
            