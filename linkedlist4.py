# Question: Rotate List

# You are given the head of a linked list.

# 👉 Rotate the list to the right by k places
class Solution:
    def rotateRight(self, head, k):
        
        if head is None or head.next is None:
            return head
        
        # Step 1: find length
        l = 1
        last = head
        
        while last.next is not None:
            last = last.next
            l += 1
        
        # Step 2: optimize k
        k = k % l
        if k == 0:
            return head
        
        # Step 3: make circular
        last.next = head
        
        # Step 4: find new tail
        curr = head
        for i in range(l - k - 1):
            curr = curr.next
        
        # Step 5: break
        head = curr.next
        curr.next = None
        
        return head
    
print(Solution().rotateRight([1, 2, 3, 4, 5], 2))