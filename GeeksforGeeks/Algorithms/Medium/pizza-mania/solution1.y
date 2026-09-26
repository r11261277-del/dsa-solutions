class Solution:
    def minimumCost(self, x, s, m, l, cs, cm, cl):
        ans = float('inf')

        # Try different numbers of small pizzas
        for small in range(x // s + 2):

            # Try different numbers of medium pizzas
            for medium in range(x // m + 2):

                area = small * s + medium * m

                if area >= x:
                    cost = small * cs + medium * cm
                    ans = min(ans, cost)
                else:
                    # Area still needed
                    remaining = x - area

                    # Number of large pizzas required
                    large = (remaining + l - 1) // l

                    cost = small * cs + medium * cm + large * cl

                    ans = min(ans, cost)

        return ans

