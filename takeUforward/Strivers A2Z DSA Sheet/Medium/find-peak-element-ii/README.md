# Find Peak Element - II

**Platform:** takeUforward  
**Category:** Strivers A2Z DSA Sheet  
**Difficulty:** Medium  
**Original Problem Link:** [Find Peak Element - II](https://takeuforward.org/practice/dsa/find-peak-element-ii?tab=solution)

---

## Performance Statistics
- **Language:** C++
- **Runtime:** N/A 
- **Memory:** N/A 

---

## Problem Description
Solution
DSA
FIND PEAK ELEMENT - II
20 MIN
Intuition: 
The brute-force solution to this problem involves searching for the largest element in the matrix by iterating through all cells. Since the question suggests that no two adjacent elements are equal, the largest element will be the peak element. However, this approach has a time complexity of O(N*M), where N is the number of rows and M is the number of columns.
To optimize the previous solution, binary search can be employed. The intuition behind the peak element in 1-D array can be used here. For each element (mid), we check if it is greater than its previous and next elements. If so, mid is identified as a peak element. Alternatively, if mid is smaller than its previous element, a peak must exist on the left side, so the right half is eliminated. Similarly, if mid is less than the next element, a peak must exist on the right side, so the left half is eliminated. This approach trims down the search space in each iteration, thereby enhancing the time complexity.
Here, for a 2-D array, the search will start from range [0, col-1], where col is the total number of columns in each row. First, find the 'mid' and find out the largest element in column 'mid' and apply the same approach as a 1-D array. That is, if the element at mid is a peak, return it. Otherwise, if the left element is greater, eliminate the right half; otherwise, eliminate the left half.
Approach: 
Working of findPeakElement(matrix):
Use two pointers, low initialized to 0 and high initialized to m - 1, to define the search range across columns.
Execute a loop where low is less than or equal to high and compute mid as (low + high) / 2 to determine the middle column.
Utilize maxElement() function to find the row index where the middle column(mid) has the maximum element and let's call it 'row'.
If element at cell(row,mid) is greater than both neighbors, return {row, mid} as the peak element coordinates.
If the left neighbor is greater than the element at cell(row,mid), adjust high to mid - 1 to search in the left half. Otherwise, adjust low to mid + 1 to search in the right half.
If the loop exits without finding a peak (i.e., low > high), return {-1, -1} to indicate no peak element exists in the matrix.

Working of maxElement(matrix,col):
Start by initializing n to arr.length, which gives the number of rows in the 2D array arr. Initialize max to Integer.MIN_VALUE to store the maximum value found in the specified column col and also initialize index to -1, which will store the index of the row containing the maximum element in the specified column.
Iterate through each row of the 2D array, find the maximum element in the column 'col' of matrix and return its index.


Dry Run
Example 1

Find Peak Element II Binary Search

Example 2

Find Peak Element II Binary Search

C++
Java
Python
JavaScript
C#
Go
1
import java.util.*;
2
3
class Solution {
4
    
5
    /* Helper function to find the index of the row
6
    with the maximum element in a given column*/
7
    public int maxElement(int[][] arr, int col) {
8
        int n = arr.length;
9
        int max = Integer.MIN_VALUE;
10
        int index = -1;
11
        
12
        /* Iterate through each row to find the
13
        maximum element in the specified column*/
14
        for (int i = 0; i < n; i++) {
15
            if (arr[i][col] > max) {
16
                max = arr[i][col];
17
                index = i;
18
            }
19
        }
20
        //Return the index
21
        return index; 
22
    }
23
    
24
    /* Function to find a peak element in 
25
    the 2D matrix using binary search */
26
    public int[] findPeakGrid(int[][] arr) {
27
        int n = arr.length;   
28
        int m = arr[0].length; 
29
        
30
        /* Initialize the lower bound for 
31
        and upper bound for binary search */
32
        int low = 0;           
33
        int high = m - 1;      
34
        
35
        // Perform binary search on columns
36
        while (low <= high) {
37
            int mid = (low + high) / 2;  
38
            
39
            /* Find the index of the row with the 
40
            maximum element in the middle column*/
41
            int row = maxElement(arr, mid);
42
            
43
            /* Determine the elements to left and 
44
            right of middle element in the found row */
45
            int left = mid - 1 >= 0 ? arr[row][mid - 1] : Integer.MIN_VALUE;
46
            int right = mid + 1 < m ? arr[row][mid + 1] : Inte

---
*Auto-committed via [GitDSA Extension](https://github.com)*
