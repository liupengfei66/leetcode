# Definition for singly-linked list.
from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head):
        if not head:
            return head
        curr, next = head, head.next
        while next:
            curr.next.next = curr 
            curr.next = None 
            curr = next 
            next = next.next 
        return curr

s = Solution()
n5 = ListNode(5)
n4 = ListNode(4, n5)
n3 = ListNode(3, n4)
n2 = ListNode(2, n3)
n1 = ListNode(1, n2)
s.reverseList(n1)