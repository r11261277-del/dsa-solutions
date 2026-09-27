# 466. Remove Duplicates From an Unsorted Linked ListPOTD

**Platform:** takeUforward  
**Category:** Linked List  
**Difficulty:** Medium  
**Original Problem Link:** [466. Remove Duplicates From an Unsorted Linked ListPOTD](https://takeuforward.org/practice/dsa/remove-duplicates-from-an-unsorted-linked-list?tab=solution)

---

## Solutions

### [solution1.java](./solution1.java)
- **Language:** Java
- **Runtime:** N/A 
- **Memory:** N/A 

---

## Problem Description
Solution
Intuition

In a simple brute-force approach, we can iterate through the list multiple times to find duplicate values. First, we would traverse the list to collect all the values in a hash map or set. Then, in a second traversal, we would remove all nodes that have values that appear more than once.

This approach is straightforward but can be inefficient, as we traverse the list multiple times.

Approach
Traverse the list and store the count of each value in a hash map (or unordered map).
Traverse the list again, and for each node, check if its value appears more than once in the hash map. If it does, delete that node.
Return the modified list.
Dry run:
Example 1

Dry run example 1

Example 2

Dry run example 2

Solution
C++
Java
Python
JavaScript
C#
Go
1
// Definition for singly-linked list.
2
class ListNode {
3
    int val;
4
    ListNode next;
5
    ListNode(int x) { val = x; }
6
}
7
 
8
class Solution {
9
    // Method to delete duplicate nodes from an unsorted linked list
10
    public ListNode deleteDuplicatesUnsorted(ListNode head) {
11
        // Step 1: Hash map to store the count of each value
12
        Map<Integer, Integer> countMap = new HashMap<>();
13
        
14
        // First pass: count occurrences of each value
15
        ListNode current = head;
16
        while (current != null) {
17
            countMap.put(current.val, countMap.getOrDefault(current.val, 0) + 1);
18
            current = current.next;
19
        }
20
 
21
        // Step 2: Second pass to remove nodes with duplicate values
22
        ListNode dummy = new ListNode(0);  // Dummy node to simplify head deletion
23
        dummy.next = head;
24
        ListNode prev = dummy;
25
        current = head;
26
        
27
        while (current != null) {
28
            if (countMap.get(current.val) > 1) {
29
                prev.next = current.next;  // Skip the current node
30
            } else {
31
                prev = current;  // Move prev to current
32
            }
33
            current = current.next;
34
        }
35
        
36
        // Step 3: Return the new head
37
        return dummy.next;
38
    }
39
}
40
 
41
public class Main {
42
    public static void main(String[] args) {
43
        Solution sol = new Solution();
44
        
45
        // Example list: 1 -> 2 -> 3 -> 2 -> 4 -> 5 -> 6 -> 4
46
        ListNode head = new ListNode(1);
47
        head.next = new ListNode(2);
48
        head.next.next = new ListNode(3);
49
        head.next.next.next = new ListNode(2);
50
        head.next.next.next.next = new ListNode(4);
51
        head.next.next.next.next.next = new ListNode(5);
52
        head.next.next.next.next.next.next = new ListNode(6);
53
        head.next.next.next.next.next.next.next = new ListNode(4);
54
        
55
        ListNode newHead = sol.deleteDuplicatesUnsorted(head);
56
        
57
        // Output the result
58
        ListNode current = newHead;
59
        while (current != null) {
60
            System.out.print(current.val + " ");
61
            current = current.next;
62
        }
63
        System.out.println();
64
    }
65
}
Complexity Analysis
Time Complexity: O(n), where n is the number of nodes in the list. We traverse the list twice (once for counting and once for removal).
Space Complexity: O(n), because we use a hash map to store the count of each value.

---
*Auto-committed via [GitDSA Extension](https://github.com)*
