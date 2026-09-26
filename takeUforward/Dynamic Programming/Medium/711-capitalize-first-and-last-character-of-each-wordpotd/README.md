# 711. Capitalize First and Last Character of Each WordPOTD

**Platform:** takeUforward  
**Category:** Dynamic Programming  
**Difficulty:** Medium  
**Original Problem Link:** [711. Capitalize First and Last Character of Each WordPOTD](https://takeuforward.org/practice/dsa/capitalize-first-and-last-character-of-each-word?tab=solution)

---

## Solutions

### [solution1.java](./solution1.java)
- **Language:** Java
- **Runtime:** N/A 
- **Memory:** N/A 

---

## Problem Description
Brute Force
Optimal
Intuition

The problem requires us to manipulate each word individually by capitalizing its first and last characters. By iterating over the string word by word, we can identify the first and last characters, convert them to uppercase, and leave the middle characters unchanged. For single-character words, simply capitalizing that character suffices. Finally, we reconstruct the string with spaces to maintain the original word separation. This approach ensures the transformation is applied correctly to all words without affecting their order.

Approach
Split the string into individual words based on spaces.
For each word, check its length:
If the word has only one character, capitalize it.
If the word has more than one character, capitalize the first and last characters while keeping the middle characters unchanged.
Combine all the transformed words back into a single string with spaces.
Return the final transformed string.
Dry Run
Example 1

Capitalize First and Last Character of Each Word - Brute

Example 2

Capitalize First and Last Character of Each Word - Brute

Code
C++
Java
Python
JavaScript
C#
Go
1
class Solution {
2
 
3
    // Capitalizes the first and last character of each word in a string
4
    public String capitalizeFirstLast(String s) {
5
        // Split the string into words
6
        String[] words = s.split(" ");
7
 
8
        // StringBuilder for the result
9
        StringBuilder result = new StringBuilder();
10
 
11
        // Process each word
12
        for (String word : words) {
13
            // Capitalize single-character words
14
            if (word.length() == 1) {
15
                word = word.toUpperCase();
16
            } else {
17
                // Capitalize first and last character
18
                word = word.substring(0, 1).toUpperCase() +
19
                       word.substring(1, word.length() - 1) +
20
                       word.substring(word.length() - 1).toUpperCase();
21
            }
22
 
23
            // Append space if not first word
24
            if (result.length() > 0) result.append(" ");
25
 
26
            // Add transformed word to result
27
            result.append(word);
28
        }
29
 
30
        // Return final string
31
        return result.toString();
32
    }
33
}
34
 
35
class Main {
36
    public static void main(String[] args) {
37
        Solution sol = new Solution();
38
        String s = "hello world a test";
39
        System.out.println(sol.capitalizeFirstLast(s));
40
    }
41
}
Time and Space Complexity
Time Complexity: O(n), where n is the length of the string. We traverse each character once while processing words and reconstructing the final string.
Space Complexity: O(n), as we store the transformed words in a new string or list, which in the worst case can be the same size as the input string.

---
*Auto-committed via [GitDSA Extension](https://github.com)*
