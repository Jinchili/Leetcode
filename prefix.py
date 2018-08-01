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