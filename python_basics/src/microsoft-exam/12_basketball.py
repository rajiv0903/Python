'''
Created on Nov 11, 2018

@author: rajiv
'''

name = input('Enter name\n')
score = 0
count = 0
sum = 0

while (score != -1):
    score = int(input('Enter Score\n'))
    if score == -1:
        break
    
    sum += score
    count += 1

average_score = sum/count

print('%-20s, your average score is %4.1f'%(name, average_score))