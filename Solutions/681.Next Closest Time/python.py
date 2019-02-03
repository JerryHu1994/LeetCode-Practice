class Solution(object):
    def nextClosestTime(self, time):
        """
        :type time: str
        :rtype: str
        """
        hr, mi = time.split(":")[0], time.split(":")[1]
        li = {int(hr[0]), int(hr[1]), int(mi[0]), int(mi[1])}
        prev_time = int(hr)*60 + int(mi)
        min_diff = float("inf")
        best_a, best_b, best_c, best_d = 0, 0, 0, 0
        for a,b,c,d in itertools.product(li, repeat = 4):
            curr_hr, curr_mi = a*10+b, c*10+d
            if curr_hr < 24 and curr_mi < 60:
                curr_time = 60*curr_hr + curr_mi
                diff = curr_time - prev_time if curr_time > prev_time else curr_time - prev_time + 24*60
                print a, b, c, d, diff
                if diff < min_diff:
                    best_a, best_b, best_c, best_d = a, b, c, d
                    min_diff = diff
        return "{}{}:{}{}".format(best_a, best_b, best_c, best_d)