# Question: Linked List Cycle

# You are given the head of a linked list.

# 👉 Determine if the linked list has a cycle
# 👉 Return True if cycle exists, otherwise False

class Solution:
    def hasCycle(self, head):
        slow = head
        fast = head
        
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:
                return True
        
        return False
    
print(Solution().hasCycle([3, 2, 0, -4])) # True
print(Solution().hasCycle([1, 2])) # True
print(Solution().hasCycle([1])) # False