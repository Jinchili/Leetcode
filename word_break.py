#Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words.
s = "leetcode"
n_list=s
wordDict = ["leet", "code"]
for i in wordDict:
    n_list=''.join(n_list.split(i))
print(n_list=='')

##it's hard to manage all the variables at once
##
def sub_check(k,s,wordDict,dict_l):
    if k==len(s):
        return True
    elif k in dict_l:
        return cacdict_l[k]
    else:
        for i in range(k,len(s)):
            if s[k:i+1] in wordDict:
                if  sub_check(i+1,s,wordDict,dict_l):
                    dict_l[k]=True
                    return True
    dict_l[k]=False
    return dict_l[k]
sub_check(0,s,wordDict,{})

##