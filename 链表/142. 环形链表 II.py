# https://leetcode-cn.com/problems/linked-list-cycle-ii/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 解法1：借助列表记录历史结点，空间复杂度不是O(1)
class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        history = []
        while head:
            if head in history:
                return head
            history.append(head)
            head = head.next
        return None

# 解法2：O(1)的解法，利用快慢指针，不过我觉得刷题如果做成数学题，意义就不是很大了
# 思路就是fast每次走2步，slow每次走一步
# 那么一定会在环内相遇，通过走的步数公式，可以推导出两者第一次相遇时情形
class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            # 如果相遇
            if slow == fast:
                p = head
                q = slow
                while p!=q:
                    p = p.next
                    q = q.next
                #你也可以return q
                return p

        return None
