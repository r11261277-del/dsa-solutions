# Maximum Nesting Depth of the Parentheses - LeetCode

**Platform:** LeetCode  
**Category:** String  
**Difficulty:** Medium  
**Original Problem Link:** [Maximum Nesting Depth of the Parentheses - LeetCode](https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/)

---

## Solutions

### [solution1.java](./solution1.java)
- **Language:** Java
- **Runtime:** 1 ms 
- **Memory:** 43.1 MB 

---

## Problem Description
Given a valid parentheses string s, return the nesting depth of s. The nesting depth is the maximum number of nested parentheses.

 
Example 1:


Input: s = "(1+(2*3)+((8)/4))+1"

Output: 3

Explanation:

Digit 8 is inside of 3 nested parentheses in the string.


Example 2:


Input: s = "(1)+((2))+(((3)))"

Output: 3

Explanation:

Digit 3 is inside of 3 nested parentheses in the string.


Example 3:


Input: s = "()(())((()()))"

Output: 3


 
Constraints:


	1 <= s.length <= 100
	s consists of digits 0-9 and characters '+', '-', '*', '/', '(', and ')'.
	It is guaranteed that parentheses expression s is a VPS.



---
*Auto-committed via [GitDSA Extension](https://github.com)*
