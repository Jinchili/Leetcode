##np arrary manipulation method
import numpy as np
def findDisappearedNumbers(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    ls_n=list(range(1,len(nums)+1))
    ls_i=[0]*len(nums)
    for i in nums:
        ls_i[i-1]=1
    ls_i=np.asarray(ls_i)
    ls_n=np.asarray(ls_n)
    return list(ls_n[ls_i==0])

##set sutract solution
def findDisappearedNumbers(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    return list(set(range(1,len(nums)+1))-set(nums))