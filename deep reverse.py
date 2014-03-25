# Question 9: Deep Reverse
# Define a procedure, deep_reverse, that takes as input a list, 
# and returns a new list that is the deep reverse of the input list.  
# This means it reverses all the elements in the list, and if any 
# of those elements are lists themselves, reverses all the elements 
# in the inner list, all the way down. 

# Note: The procedure must not change the input list.

# The procedure is_list below is from Homework 6. It returns True if 
# p is a list and False if it is not.

def is_list(p):
    return isinstance(p, list)

def copy(testing):
    newreverse2=[]
    i=0
    while i<len(testing):
      newreverse2.append(testing[i])
      i=i+1
    return newreverse2


def reverse(testing):
    newreverse2=[]
    i=1
    while i<len(testing)+1:
      newreverse2.append(testing[-i])
      i=i+1
    return newreverse2

def m_reverse(testing):
    if is_list(testing)==True:
        return reverse(testing)
    else:
        m_reverse(testing)
        
def deep_copy(x):
    if not isinstance(x, list): return x
    else: return map(deep_copy, x)

def deep2_reverse(a):
    b=reverse(a)
    for i in b:
        if is_list(i):
            deep_reverse(i)  # <=== This is what changed
    return b  

def deep_reverse(a):
    b=deep_copy(a)
    return p_reverse(b)
    
def p_reverse(a):
    a.reverse()
    for i in a:
        if is_list(i):
            p_reverse(i)
            print i
    return a

  



#For example,
p=[1, [2, 3]]
print deep_reverse(p)
print p

#p = [1, [2, 3, [4, [5, 6]]]]
#print deep_reverse(p)
#>>> [[[[6, 5], 4], 3, 2], 1]
#print p
#>>> [1, [2, 3, [4, [5, 6]]]]

#q =  [1, [2,3], 4, [5,6]]
#print deep_reverse(q)
#>>> [ [6,5], 4, [3, 2], 1]
#print q
#>>> [1, [2,3], 4, [5,6]]
