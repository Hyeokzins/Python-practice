def t_list(two_list):
    return[row for row in zip(*two_list)]
 
print(t_list([[1,4,7], [2,5,8], [3,6,9]]))