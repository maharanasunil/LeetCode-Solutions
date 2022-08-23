# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        
		#vList = valueList
        vList = [] 
		
		#Converting to list
        while head != None:
            if head.val == 0:
                vList.append(0)
            else:
                vList.append(head.val)
            head = head.next
        
		#nList = newList which will be reverse of vList
        nList = vList[::-1]
        
		#Checking for Palindrome!
        if nList == vList:
            return True
        else:
            return False