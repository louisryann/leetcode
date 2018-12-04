'''
给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，
并且它们的每个节点只能存储 一位 数字。
如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。
您可以假设除了数字 0 之外，这两个数都不会以 0 开头。
'''

'''解析：
本题可以把链表中的元素转换为相应的数据后进行相加，得到的结果在按照相应的格式放入链表中。 
也可以直接按照链表的方式进行相加，在相加的过程中判断其是否要进位，如果需要进位是向后进位的。
'''

#思路:可以使用递归，每次算一位的相加

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1:
            return l2     #在python中 None,  False, 空字符串"", 0, 空列表[], 空字典{}, 空元组()都相当于False
        if not l2:
            return l1

        if l1.val+l2.val < 10:
            l3 = ListNode(l1.val+l2.val)
            l3.next = self.addTwoNumbers(l1.next,l2.next)
        else:
            l3 = ListNode(l1.val+l2.val-10)
            tmp = ListNode(1)
            tmp.next = None
            l3.next = self.addTwoNumbers(l1.next,self.addTwoNumbers(l2.next,tmp))

        return l3

