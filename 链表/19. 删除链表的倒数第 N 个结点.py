# https://leetcode-cn.com/problems/remove-nth-node-from-end-of-list/
# 倒数N步，用快慢指针比较好，两者之间相差N+1步，保证慢指针在待删除结点前，方便操作
# 同时，增加虚拟头结点，保证行为一致性
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        root = ListNode(next=head)
        slow, fast = root, root
        # 快指针先走N+1步，保证快指针到结尾，慢指针在倒数N+1个位置
        for i in range(n+1, 1, -1):
            fast = fast.next
        while fast:
            fast = fast.next
            slow = slow.next
        # 删除结点
        slow.next = slow.next.next
        return root.next