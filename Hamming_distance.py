####The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

##Given two integers x and y, calculate the Hamming distance.
def hammingDistance( x, y):
    """
    :type x: int
    :type y: int
    :rtype: int
    """
    return bin(x^y).count("1")


##binary tree merge
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def mergeTrees(t1, t2):
    """
    :type t1: TreeNode
    :type t2: TreeNode
    :rtype: TreeNode
    """
    if not t1 or not t2:
        return t2 or t1
    merged=TreeNode(t1.val+t2.val)
    merged.left=self.mergeTrees(t1.left,t2.left)
    merged.right = self.mergeTrees(t1.right, t2.right)
    return merged

###find the single value [set() function can make a dictionary for unique values]
def singleNumber(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    noduplicated_list=[]
    for item in nums:
        try:
            noduplicated_list.remove(item)
        except:
            noduplicated_list.append(item)
    return noduplicated_list.pop()


a_string=")(1,2,3,4(,5))"

def del_quo(a_string):
    if a_string ==None:
        return None
    d_pair=[]
    del_list=[]
    for i in range(len(a_string)):
        if a_string[i] =="(":
            d_pair=d_pair+[i]
        elif a_string[i] ==")":
            if d_pair !=[]:
                del_list=del_list+[d_pair.pop()]+[i]
    b_list=''
    for j in range(len(a_string)):
        if j not in del_list:
            b_list=b_list+a_string[j]
    return str(b_list)