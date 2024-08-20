"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    '''
    Time Complexity: O(N), where N is the number of nodes in the tree
    Space Complexity: O(1)

    '''
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        curr, nxt = root, root.left if root else None
        while curr and nxt:
            curr.left.next = curr.right
            if curr.next:
                curr.right.next = curr.next.left
            curr = curr.next
            if not curr:
                curr = nxt
                nxt = curr.left
        return root
