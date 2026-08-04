# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, d: Optional[ListNode]) -> bool:
    
        itr = d
        visited = set()

        while itr:
            if itr in visited:
                return True

            visited.add(itr)
            itr = itr.next

        return False
