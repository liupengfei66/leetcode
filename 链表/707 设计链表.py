# https://leetcode-cn.com/problems/design-linked-list/submissions/
# 设置尾结点，会提高在尾部插入的效率，但是代码需要注意尾结点发生变动时，要及时更新
# 从代码角度，还是不设置尾结点，更不容易出错
# 结点箭头顺序与代码顺序一致，箭头从a->b，代码也是a=b
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class MyLinkedList:

    def __init__(self):
        self.len = 0
        self.root = ListNode(0, None)

    def get(self, index: int) -> int:
        if index < 0 or index >= self.len:
            return -1

        curr = self.root
        for _ in range(index+1):
            curr = curr.next
        return curr.val

    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.len, val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.len:
            return
        if index < 0:
           index = 0

        curr = self.root
        for _ in range(index):
            curr = curr.next
        curr.next = ListNode(val, curr.next)
        self.len += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.len:
            return
        curr = self.root
        for _ in range(index):
            curr = curr.next
        curr.next = curr.next.next
        self.len -= 1



# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)