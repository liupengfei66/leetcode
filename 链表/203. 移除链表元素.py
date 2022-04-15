# https://leetcode-cn.com/problems/remove-linked-list-elements/
# 设置虚拟头结点，可以保证所有节点的行为一致
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        root = ListNode(val=0, next=head)
        curr = root
        while curr.next:
            if curr.next.val == val:
                curr.next = curr.next.next
            else:
                curr = curr.next
        return root.next