#find the maximum gap following the order
def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    if prices==[]:
        return 0
    max_p=0
    min_n=prices[0]
    for i in prices:
        if i<min_n:
            min_n=i
        elif i-min_n>max_p:
            max_p=i-min_n
    return max_p
##climbStairs with 1 steps or 2 steps
#given n there is at most x=n//2 number of 2 steps which is x different way
#for x number of 2 steps, there left with n-x 1 steps. it's a combination problem. 


from math import factorial as fac
def climbStairs(n):
    """
    :type n: int
    :rtype: int
    """
    #if n==None:
    #    return 0
    n_2=n//2
    n_sum=0
    for i in range(n_2+1):
        n_1=n-2*i
        n_t=n_1+i
        n_sum += fac(n_t)/(fac(n_1)*fac(i))
    return n_sum
            

##recursion solution
def climbStairs(n):
    """
    :type n: int
    :rtype: int
    """
    #if n==None:
    #    return 0
    if n==1 :
        return 1
    elif n==2 :
        return 2
    else :
        return climbStairs(n-1)+climbStairs(n-2)
    




##3 sum to zeros

a=[1,2,2,-1,-2,3]
def threeSum(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    if len(nums) < 3:
        return []
    nums.sort()
    res = set()
    for i, v in enumerate(nums[:-2]):
        if i >= 1 and v == nums[i-1]:
            continue
        d = {}
        for x in nums[i+1:]:
            if x not in d:
                d[-v-x] = 1
            else:
                res.add((v, -v-x, x))
    return map(list, res)
threeSum(a)