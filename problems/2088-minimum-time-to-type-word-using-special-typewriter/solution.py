class Solution:
    def minTimeToType(self, word):
        current = 'a'
        time = 0

        for ch in word:
            distance = abs(ord(ch) - ord(current))
            move = min(distance, 26 - distance)

            time += move + 1
            current = ch

        return time
