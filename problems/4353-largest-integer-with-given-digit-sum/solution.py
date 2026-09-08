class Solution:
    def largestInteger(self, n, s):
        if s > 9 * n:
            return -1

        if s == 0:
            return 0

        result = ""

        for i in range(n):
            if s >= 9:
                result += "9"
                s -= 9
            else:
                result += str(s)
                s = 0

        return int(result)
