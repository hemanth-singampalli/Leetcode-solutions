class Solution:
    def maxDistance(self, colors):
        n = len(colors)
        answer = 0

        for i in range(n):
            if colors[i] != colors[0]:
                answer = max(answer, i)

            if colors[i] != colors[n - 1]:
                answer = max(answer, n - 1 - i)

        return answer
