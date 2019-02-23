'''
输入一个链表，按链表值从尾到头的顺序返回一个ArrayList。
'''
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

'''
方法一：短小精悍，每次都是调用list的insert函数，将元素插入第一个位置，然后返回的自然就是倒序的list列表
'''
# def printListFromTailToHead(listNode):
#     l=[]
#     head=listNode
#     while head is not None:
#         l.insert(0,head.val)
#         head=head.next
#     return l

'''
方法二：正序插入，返回list的时候使用切片，从最后一个返回，依然是倒序
'''
def  printListFromTailToHead(listNode):
    l=[]
    head=listNode
    while head is not None:
        l.append(head.val)

    return l[::-1]
