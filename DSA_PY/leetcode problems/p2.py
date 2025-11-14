# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        self.l1 = l1
        self.l2 = l2
        m1 = len(l1)-1
        m2 = len(l2)-1
        n1 = 0
        n2 = 0
        while m1>=0:
            n1 += l1[m1]*(10**m1)
            m1-=1
        while m2>=0:
            n2 += l2[m2]*(10**m2)
            m2-=1
        sum = n1+n2
        r = []
        while sum>0:
            r.append(sum%10)
            sum = sum//10
        return r

