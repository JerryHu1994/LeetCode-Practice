class Solution:
    def interpret(self, command: str) -> str:
        curr, res = 0, ''
        while curr < len(command):
            if command[curr] == 'G':
                res += 'G'
                curr += 1
            elif command[curr:curr+2] == '()':
                res += 'o'
                curr += 2
            elif command[curr:curr+4] == '(al)':
                res += 'al'
                curr +=4
        return res
            