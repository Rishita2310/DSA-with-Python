# Question: Remove Duplicates from Sorted List

# You are given the head of a sorted linked list.

# 👉 Remove all duplicates such that each element appears only once
# 👉 Return the updated linked list
class Solution:
    def deleteDuplicates(self, head):
        
        # Corner case
        if head is None or head.next is None:
            return head
        
        curr = head
        
        while curr is not None and curr.next is not None:
            
            # Duplicate found
            if curr.val == curr.next.val:
                curr.next = curr.next.next
            else:
                curr = curr.next
        
        return head
    
print(Solution().deleteDuplicates([1, 1, 2, 3, 3]))