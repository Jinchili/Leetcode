
##rob maximum profitable two stores
def rob(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    dp = []
    for i, v in enumerate(nums):           
        dp.append(max(
            dp[i-1] if len(dp) >= 1 else 0,    ##choose biger one in every two store
            dp[i-2] + v if len(dp) >= 2 else v
        ))            

    return dp[-1] if dp else 0

##search and insert a sorted list
def searchInsert(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    i=0
    try:
        value=nums.index(target)
    except ValueError:
        while target>nums[i]:
            i=i+1
            if i>(len(nums)-1):
                value=i
                break
        value=i
    return value