# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        a = l1
        b = l2 
        arr1 = []
        arr2 = []

        while a:
          arr1.append(a.val)
          a = a.next

        while b:
          arr2.append(b.val)
          b = b.next

        arr1.reverse()
        arr2.reverse()

        inta = int("".join(str(x) for x in arr1)) 
        intb = int("".join(str(x) for x in arr2))

        c = list(str(inta + intb)) 

        
        head = l3 = ListNode(c.pop())

        c.reverse()

        
        for i in c:
            l3.next = ListNode(i)
            l3 = l3.next

        return head 
        
        