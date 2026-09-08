class Solution:
    def convertTime(self, current, correct):
        h1, m1 = map(int, current.split(":"))
        h2, m2 = map(int, correct.split(":"))

        current_minutes = h1 * 60 + m1
        correct_minutes = h2 * 60 + m2

        difference = correct_minutes - current_minutes

        operations = 0

        for x in [60, 15, 5, 1]:
            operations += difference // x
            difference %= x

        return operations
