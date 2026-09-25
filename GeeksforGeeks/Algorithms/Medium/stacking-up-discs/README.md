# Maximum Height Disc Stack

**Platform:** GeeksforGeeks  
**Category:** Algorithms  
**Difficulty:** Medium  
**Original Problem Link:** [Maximum Height Disc Stack](https://www.geeksforgeeks.org/problems/stacking-up-discs1315/1)

---

## Performance Statistics
- **Language:** def maxStackHeight(self, r, h):
        from bisect import bisect_left

        class FenwickTree:
            def __init__(self, n: int) -> None:
                self.n = n + 1
                self.bit = [0] * self.n

            def query(self, idx: int) -> int:
                res = 0
                while idx:
                    res = max(res, self.bit[idx])
                    idx -= idx & -idx
                return res

            def update(self, idx: int, val: int) -> None:
                while idx < self.n:
                    self.bit[idx] = max(self.bit[idx], val)
                    idx += idx & -idx

        n = len(r)
        order = sorted(range(n), key = lambda i: (r[i], -h[i]))
        heights = sorted(set(h))
        max_height = -1
        ft = FenwickTree(len(heights))
        for i in order:
            radius, height = r[i], h[i]
            h_idx = bisect_left(heights, height)
            max_sub_height = ft.query(h_idx)
            curr_height = max_sub_height + height
            ft.update(h_idx + 1, curr_height)
            max_height = max(max_height, curr_height)
        return max_height
- **Runtime:** N/A 
- **Memory:** N/A 

---

## Problem Description
Problem statement: Maximum Height Disc Stack

---
*Auto-committed via [GitDSA Extension](https://github.com)*
