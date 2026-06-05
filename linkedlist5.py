# Question: Intersection of Two Linked Lists

# You are given heads of two singly linked lists: headA and headB.

# 👉 Return the node where the two lists intersect
# 👉 If they do not intersect → return None
class Solution:
    def getIntersectionNode(self, headA, headB):
        p1 = headA
        p2 = headB
        
        while p1 != p2:
            p1 = p1.next if p1 else headB
            p2 = p2.next if p2 else headA
        
        return p1
    
print(Solution().getIntersectionNode([1, 2, 3], [4, 5, 6]))