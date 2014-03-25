
p_c=.1
p_pos_c=.9
p_neg_nc=.8
p_nc=1-p_c
p_neg_c=1-p_pos_c
p_pos_nc=1-p_neg_nc


A=p_c*p_pos_c
B=p_nc*p_pos_nc
C=A+B
print p_c
print p_pos_c
print p_nc
print p_pos_nc
print A
print B
print A/C
print B/C