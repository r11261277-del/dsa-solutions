class Solution {
    // Method to delete duplicate nodes from an unsorted linked list
    public ListNode deleteDuplicatesUnsorted(ListNode head) {
        // Step 1: Hash map to store the count of each value
        Map<Integer, Integer> countMap = new HashMap<>();
        
        // First pass: count occurrences of each value
        ListNode current = head;
        while (current != null) {
            countMap.put(current.val, countMap.getOrDefault(current.val, 0) + 1);
            current = current.next;
        }

        // Step 2: Second pass to remove nodes with duplicate values
        ListNode dummy = new ListNode(0);  // Dummy node to simplify head deletion
        dummy.next = head;
        ListNode prev = dummy;
        current = head;
        
        while (current != null) {
            if (countMap.get(current.val) > 1) {
                prev.next = current.next;  // Skip the current node
            } else {
                prev = current;  // Move prev to current
            }
            current = current.next;
        }
        
        // Step 3: Return the new head
        return dummy.next;
    }
}