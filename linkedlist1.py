# Question: Remove Nth Node From End of List

# You are given the head of a linked list.

# 👉 Remove the nth node from the end of the list and return the updated head.

class Solution:
    def removeNthFromEnd(self, head, n):
        p1 = head
        p2 = head

        # Move p2 ahead by n steps
        for i in range(n):
            p2 = p2.next

        # If we need to remove the first node
        if p2 is None:
            return head.next

        # Move both pointers
        while p2.next is not None:
            p2 = p2.next
            p1 = p1.next

        # Remove node
        p1.next = p1.next.next

        return head
    
print(Solution().removeNthFromEnd([1, 2, 3, 4, 5], 2))  