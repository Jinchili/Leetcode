##list##
a=[]
a.append('a')   ##****
a.insert(5,'a') ###this will be the latest position  ****
a.pop()  ##return the last item in the list    *****
a.pop(i)  ##return i th item in the list
a.sort()  ##Modifies a list to be sorted
a.reverse()  ##reverse the list
del a[i] ##delete i the element 
a.index("a") ##return the first index of occurence of item
a.count('a') ##return the number of item
a.remove('a') ##remove the first occurance of item 'a'

##string##
myname='jinchi'
myname.upper()
myname.lower()
myname.center(w) ##return a string with lenth w which ensure myname is in the center
myname.split("i")


##set##
myskill={'python','R','SQL','Pytorch'}
required_skill={"python",'R'}
required_skill <= myskill
required_skill | myskill
required_skill & myskill

myskill.add('Tensorflow')
myskill.remove("cool")
myskill.pop()
myskill.clear() ##delete all element

##dictionary##
myskill_set={'python':'expert','R':"expert",'SQL':'expert'}
myskill_set.keys()
myskill_set.values()

##input##
aName = input('Please enter your name: ')

##string formating3#
print(myskill, sep="***")
print("%s is %d years old." % (aName, age))


##converting infix to posfix
a='(A+B)*(C+D)*(E+F)'
c='A*B*C*D+E+F'

prior_set={}
prior_set['*']=3
prior_set['/']=3
prior_set['+']=2
prior_set['-']=2
prior_set['(']=1

def posfix_f (str_e):
    prior_set={}
    prior_set['*']=3
    prior_set['/']=3
    prior_set['+']=2
    prior_set['-']=2
    prior_set['(']=1    
    out_list=[]
    a_stack=[]
    for i in str_e:
        if i in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' or i in '0123456789':
            out_list+=[i]
        elif i=="(" :
            a_stack+=[i]
        elif i==')':
            top_token=a_stack.pop()
            while top_token != "(":
                out_list+=[top_token]
                top_token=a_stack.pop()
        else:
            while a_stack!=[] and prior_set[a_stack[-1]]>=prior_set[i]:
                out_list+=a_stack.pop()
            a_stack+=[i]
    while a_stack !=[]:
        out_list+=a_stack.pop()
    return ''.join(out_list)


a='A*B+C*D'
def prefix_f (str_e):
    prior_set={}
    prior_set['*']=3
    prior_set['/']=3
    prior_set['+']=2
    prior_set['-']=2
    prior_set['(']=1    
    out_list=[]
    a_stack=[]
    for i in str_e:
        if i in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' or i in '0123456789':
            out_list+=[i]
        elif i=="(" :
            a_stack+=[i]
        elif i==')':
            top_token=a_stack.pop()
            while top_token != "(":        ##there is at least one operation inside of the ()
                out_list_n= top_token+out_list.pop(-2)+out_list.pop(-1)
                out_list+=[out_list_n]
                top_token=a_stack.pop()
        else:
            while a_stack!=[] and prior_set[a_stack[-1]]>=prior_set[i]:
                out_list_n= a_stack.pop()+out_list.pop(-2)+out_list.pop(-1)
                out_list+=[out_list_n]
            a_stack+=[i]
    while a_stack !=[]:
        out_list_n= a_stack.pop()+out_list.pop(-2)+out_list.pop(-1)
        out_list+=[out_list_n]        
    return ''.join(out_list)

prefix_f(a)