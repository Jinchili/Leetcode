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
