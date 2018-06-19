import numpy as np
###suppose to return pairs inside of list which add up to target value
def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    nums=np.array(nums)
    pos_num=nums[np.array(nums)<target]
    com_num=target-pos_num
    id_num= np.isin(com_num,pos_num)*(com_num < pos_num)
    return [np.asscalar(pos_num[id_num]),np.asscalar(com_num[id_num])]
###loop overt it 
def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    for i in nums:
        if (target-i) in nums : return [i,target-i]
    return

###if output index##
def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    dict = {}
    for i in range(len(nums)):
        if target-nums[i] not in dict:
            dict[nums[i]]=i
        else:
            return [dict[target-nums[i]],i]
        
        
##
def isValid(s):
    """
    :type s: str
    :rtype: bool
    """
    flag=False
    dir_in={"{":"}","[":"]","(":")"}
    n=len(s)
    if n%2==1: return "e1"
    num=int(n/2)
    for i in range(num):
        if s[i] in dir_in and s[2*num-i-1] != dir_in[s[i]]: return "e2"
        if s[i] not in dir_in: return "e3"
    return "t4"
        
##to figure out the "()" are used correctly : sequence, close
def isValid(self, s):
    """
    :type s: str
    :rtype: bool
    """
    flag=True
    dir_in={"{":"}","[":"]","(":")"}
    dir_in={v:k for k,v in dir_in.items()}
    n=len(s)
    if n%2==1: return False
    stack=[]
    for char in s:
        if char in dir_in.values() :
            stack+=[char]
        elif char in dir_in.keys():
            if stack==[]: 
                flag=False
                break
            elif stack.pop() != dir_in[char]:
                flag=False
                break
            else:
                continue
        else:
            flag=False
            break
    if stack!=[]:
        flag=False
    return flag
                    
            
