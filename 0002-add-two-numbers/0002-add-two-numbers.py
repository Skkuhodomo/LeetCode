# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def list2Node(self, list1:list) -> ListNode:
        result = ListNode()
        for i, num in enumerate(list1):
            if i == 0:
                result.val = num
            else: 
                node = result
                while node.next != None:
                    node = node.next
                node.next = ListNode(num)
        return result 
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        a1 = []
        a2 = []
        n1,n2,j,k = 0
        while l1 != None:
            a1.append(l1.val)
            l1 = l1.next 
        while l2 != None:
            a2.append(l2.val)
            l2 = l2.next 
        for i in a1:
            n1 += i*(10**(j))
            j += 1
        for i in a2:
            n2 += i*(10**(k))
            k +=1 
        sum_num = n1+n2
        sum_str = list(str(sum_num))
        sum_str.reverse()
        print(sum_str, " ",n1," ", n2 )

        return self.list2Node(sum_str)