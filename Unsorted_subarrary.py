##Given an integer array, you need to find one continuous subarray that if you only sort this subarray in ascending order, then the whole array will be sorted in ascending order, too.
##You need to find the shortest such subarray and output its length
import numpy as np

def findUnsortedSubarray( nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    sort_list=sorted(nums)
    diff_list=np.array(sort_list)-np.array(nums)
    diff_list=diff_list!=0
    diff_list=list(diff_list)
    n=len(diff_list)
    if sum(diff_list)==0: return 0
    start=diff_list.index(True)
    diff_list.reverse()
    end=n-diff_list.index(True)
    return end-start

##intersection of two linked list
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
def getIntersectionNode(headA, headB):
    """
    :type head1, head1: ListNode
    :rtype: ListNode
    """
    if (headA)==None or (headB)==None:
        return None
    pointA=headA
    pointB=headB
    while pointA!=pointB:
        if (pointA ==None) and (pointB ==None):
            return None
        elif pointA ==None:
            pointA=headB
            pointB=pointB.next
        elif pointB ==None:
            pointB=headA
            pointA=pointA.next
        else:
            pointA =pointA.next
            pointB =pointB.next
    return pointA