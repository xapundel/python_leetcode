from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def print(self):
        tmp = self
        while tmp != None:
            print(tmp.val)
            tmp = tmp.next



class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Need to return new ordered linked list consists of two existed
        """
        cur = dummy = ListNode()
        while list1 and list2:               
            if list1.val < list2.val:
                cur.next = list1
                cur = list1
                list1 = list1.next
                # list1, cur = list1.next, list1
            else:
                cur.next = list2
                cur = list2
                list2 = list2.next
                # list2, cur = list2.next, list2
                
        if list1 or list2:
            cur.next = list1 if list1 else list2
            
        return dummy.next






        #recursive solution
        # if list1 == None:
        #     return list2
        # if list2 == None:
        #     return list1

        # if (list1.val <= list2.val):
        #     list1.next = self.mergeTwoLists(list1.next, list2)
        #     return list1
        # else :
        #     list2.next = self.mergeTwoLists(list1, list2.next)
        #     return list2
        

list1 = ListNode(1,ListNode(2,ListNode(4, ListNode(6))))
list2 = ListNode(1,ListNode(3,ListNode(4)))

# list1.print()
# list2.print()
s = Solution()
res = s.mergeTwoLists(list1, list2)

res.print()