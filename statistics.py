import math
import random
from math import sqrt

p_c=.1
p_pos_c=.9
p_neg_nc=.8
p_nc=1-p_c
p_neg_c=1-p_pos_c
p_pos_nc=1-p_neg_nc


A=p_c*p_pos_c
B=p_nc*p_pos_nc
C=A+B
#print p_c
#print p_pos_c
#print p_nc
#print p_pos_nc
#print A
#print B
#print A/C
#print B/C

def binomial(n,k):
  return long(math.factorial(n))/(math.factorial(n-k)*math.factorial(k))


i=1

#print binomial(i,0)
#print binomial(i,1)
#print binomial(i,2)
#  print binomial(i,3)

def mean(data):
  return float(sum(data))/len(data)
  
def variance(data):
  mu=mean(data)
  return sum([(x-mu)**2 for x in data])/len(data)  
  

def stddev(data):
  return sqrt(variance(data))
  
def flip_clike(N):
    r=[]
    i=0
    while i<N:
      e=random.random()
      if e<.5:
        e=0
      if e>.5:
        e=1
      r.append(e)
      i=i+1
    return r

def flip(N):
    return [random.random()>0.5 for x in range(N)]        
  
#N=1000
#f=flip(N)

#print mean(f)
#print stddev(f)

hey=[5,9,100,9,97,6,9,98,9]
print mean(hey)

