##definition:binary tree: left nodes <right nodes:
##space complexicity O(N),
####
##second level:time and space complexity
##approach summary
##similar problem
##merge sort vs quick sort


##clarify
##appeoach
##input/output/helper reference to pass through
##assumption:corner case/edge case/base case
##comment + code + review
##time complexity
##space complexity
def linear_search(data,target):
    for i in data:
        if t == target:
            return true
    return False
###sorted list£¨O£¨logn£©£©
def binary_search_iterative(data,target):
    n=len(data)
    low=0
    high=n-1
    
    while low<=high:
        mid=(low+high)//2
        if target>data[mid]:
            low=mid+1
        elif target<data[mid]:
            high=mid-1
        else:   
            return mid
    return False
####