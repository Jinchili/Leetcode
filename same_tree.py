#Given two binary trees, write a function to check if they are the same or not.
def isSameTree(self, p, q):
    if not p and not q :
        return True
    elif (p and q) and (p.value==q.value) and \
        self.isSameTree(p.left,q.left) and \
        self.isSameTree(p.right,q.right):
        return True
    else:
        return False


##A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).
##The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).
##How many possible unique paths are there?
    ##Sloution 1 :this is a combination problem
    
def uniquePaths(m, n):
    """
    :type m: int
    :type n: int
    :rtype: int
    """
    total_s=m+n-2
    total_p=1
    total_d=1
    for i in range(n-1):
        total_p*=total_s-i
    total_d=1
    for j in range(1,n):
        total_d*=j
    return total_p/total_d

##calculate the score as descprited
def calPoints(self, ops):
    """
    :type ops: List[str]
    :rtype: int
    """
    n=len(ops)
    score=0
    score_l=[]
    if not ops:
        return 0
    else:
        for i in ops:
            if i == 'C':
                score_l.pop()
            elif i =='D':
                score_l += [2*score_l[-1]]
            elif i =='+':
                score_l += [score_l[-1]+score_l[-2]]
            else:
                score_l += [int(i)]
    return sum(score_l)