class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        secret_nums, guess_nums = [int(i)   for i in secret], [int(i)   for i in guess]
        l = len(secret_nums)
        bull = sum([secret_nums[i] == guess_nums[i]  for i in range(l)])
        cnt = collections.Counter([secret_nums[i]    for i in range(l) if secret_nums[i] != guess_nums[i]])
        cow = 0
        for i in range(l):
            if secret_nums[i] != guess_nums[i]:
                if guess_nums[i] in cnt:
                    cow += 1
                    cnt[guess_nums[i]] -= 1
                    if cnt[guess_nums[i]] == 0: del cnt[guess_nums[i]]
        return str(bull)+"A"+str(cow)+"B"