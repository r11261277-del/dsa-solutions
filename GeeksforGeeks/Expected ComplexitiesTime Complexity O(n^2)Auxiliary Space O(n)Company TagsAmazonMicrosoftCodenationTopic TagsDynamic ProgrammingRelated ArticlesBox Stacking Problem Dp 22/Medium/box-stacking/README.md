# C++ Solution  ||  Easy Approach and Step by Step Explanation

**Platform:** GeeksforGeeks  
**Category:** Expected ComplexitiesTime Complexity: O(n^2)Auxiliary Space: O(n)Company TagsAmazonMicrosoftCodenationTopic TagsDynamic ProgrammingRelated ArticlesBox Stacking Problem Dp 22  
**Difficulty:** Medium  
**Original Problem Link:** [C++ Solution  ||  Easy Approach and Step by Step Explanation](https://www.geeksforgeeks.org/problems/box-stacking/1)

---

## Performance Statistics
- **Language:** def maxHeight(self, height: list[int], width: list[int], length: list[int]) -> int:
        # Code here
        boxes = []
        for h, w, l in zip(height, width, length):
            boxes.extend([(min(w, l), max(w, l), h), (min(w, h), max(w, h), l), (min(h, l), max(h, l), w)])
            
        n = len(boxes)
        dp = [0]*n
        
        boxes.sort(key=lambda c: (c[0], c[1]))

        ans = 0
        for i, (s, b, h) in enumerate(boxes):
            dp[i] = h
            for j in range(i):
                if boxes[j][0] < s and boxes[j][1] < b:
                    dp[i] = max(dp[i], dp[j] + h)
            ans = max(ans, dp[i])
        return ans
- **Runtime:** N/A 
- **Memory:** N/A 

---

## Problem Description
Problem statement: C++ Solution  ||  Easy Approach and Step by Step Explanation

---
*Auto-committed via [GitDSA Extension](https://github.com)*
