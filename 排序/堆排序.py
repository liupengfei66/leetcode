import random

# 调整列表中的元素并保证以root为根的堆是一个大根堆
def adjust_max_heap(heap, heapSize, root):  
    '''
    给定某个节点的下标root，这个节点的父节点、左子节点、右子节点的下标都可以被计算出来。
    父节点：(root-1)//2
    左子节点：2*root + 1
    右子节点：2*root + 2  即：左子节点 + 1
    '''
    left = 2*root + 1
    right = left + 1
    larger = root
    # 比较root和左右子孩子的大小，把最大的升级为root
    if left < heapSize and heap[larger] < heap[left]:
        larger = left
    if right < heapSize and heap[larger] < heap[right]:
        larger = right
    # 如果做了堆调整则larger的值等于左节点或者右节点的值，这个时候做堆调整操作，交换此时的最大值到root节点
    if larger != root:  
        heap[larger], heap[root] = heap[root], heap[larger]
        # 递归的对子树做调整
        # 注意，此处不用对另外一个子树调整，因为大顶堆不需要比较兄弟之间的大小
        # 因为当前子树是被替换了一个较小的值，所以才需要重新调整
        # 如果没有被替换，那么在建堆时，该子树已经满足大顶堆的条件了，不需要调整
        adjust_max_heap(heap, heapSize, larger)
        
def heap_sort(heap):  
    heapSize = len(heap)
    # 1. 自底向上，自右到左，构建一个大顶堆
    # heapSize-1是二叉树的最后一个叶结点，其父节点是(heapSize-1-1)//2
    for i in range((heapSize-2)//2, -1, -1):  
        adjust_max_heap(heap, heapSize, i)
    
    # 2. 第一个元素就是这个列表中最大的元素，将其与最后一个元素交换
    # 然后将剩余的列表再调整为最大堆
    for i in range(len(heap)-1, -1, -1):
        heap[0], heap[i] = heap[i], heap[0]
        adjust_max_heap(heap, i, 0)


if __name__ == '__main__':
    a = [30, 50, 57, 77, 62, 78, 94, 80, 84]
    print(a)
    heap_sort(a)
    print(a)
    b = [random.randint(1,10) for i in range(10)]
    print(b)
    heap_sort(b)
    print(b)
#
# [30, 50, 57, 77, 62, 78, 94, 80, 84]
# [30, 50, 57, 62, 77, 78, 80, 84, 94]
# [1, 8, 8, 4, 7, 1, 7, 4, 7, 9]
# [1, 1, 4, 4, 7, 7, 7, 8, 8, 9]