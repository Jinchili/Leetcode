###inverse a int in +-2**31, for outrange return 0
def reverse(x):
    """
    :type x: int
    :rtype: int
    """
    threshold=2**31
    if x==0 or (x not in range(-threshold,threshold)) :
        return 0
    elif x>0:
        x_str=str(x)
        value=int(x_str[::-1])
        if value> (threshold-1) : return 0
        else : return value
    else:
        x_str=str(-x)
        value=int(x_str[::-1])
        if value> threshold : return 0
        else : return -value


##check if it's possible to make it non-decreasing arrary by modify at most 1 element
##strs could use sorted function to become a list of sorted char
        