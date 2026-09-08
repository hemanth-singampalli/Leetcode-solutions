class Solution:
    def distMoney(self, money, children):
        # Give every child $1
        money -= children

        # Not enough money
        if money < 0:
            return -1

        # Maximum children that can get 8 dollars
        ans = min(money // 7, children)

        # Money left after making ans children get $8
        money -= ans * 7

        # All children have $8, but extra money remains
        if ans == children and money > 0:
            ans -= 1

        # One child is left, and exactly $3 extra would make
        # that child receive $4, which is not allowed
        elif ans == children - 1 and money == 3:
            ans -= 1

        return ans
