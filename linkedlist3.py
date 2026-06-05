# Question: Reverse Linked List

# You are given the head of a singly linked list.
class Solution:
    def reverseList(self, head):
        curr = head
        prev = None
        
        while curr is not None:
            nxt = curr.next      # store next
            curr.next = prev     # reverse link
            prev = curr          # move prev
            curr = nxt           # move curr
        
        return prev
print(Solution().reverseList([1, 2, 3, 4, 5]))