            countMap.put(current.val, countMap.getOrDefault(current.val, 0) + 1);
            current = current.next;
        }

        // Step 2: Second pass to remove nodes with duplicate values
        ListNode dummy = new ListNode(0);  // Dummy node to simplify head deletion
        dummy.next = head;
        ListNode prev = dummy;
        current = head;
        
        while (current != null) {
            if (countMap.get(current.val) > 1) {
                prev.next = current.next;  // Skip the current node