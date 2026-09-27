        // Step 1: Hash map to store the count of each value
        Map<Integer, Integer> countMap = new HashMap<>();
        
        // First pass: count occurrences of each value
        ListNode current = head;
        while (current != null) {
            countMap.put(current.val, countMap.getOrDefault(current.val, 0) + 1);
            current = current.next;
    // Method to delete duplicate nodes from an unsorted linked list
    public ListNode deleteDuplicatesUnsorted(ListNode head) {

class Solution {