'''
Created on Nov 11, 2018
@author: rajiv
'''

productIdList = [0,1,2,3,4,5,6,7,8,9]
index = 0

while index<10:
    print(productIdList[index])
    if productIdList[index] == 6:
        break;
    else:
        index += 1;
