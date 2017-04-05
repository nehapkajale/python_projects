'''
Read the triangle from triangle.txt file and find maximum sum

By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.
3
7 4
2 4 6
8 5 9 3
That is: 3 + 7 + 4 + 9 = 23

'''

import time


start  = time.time()
f = open('triangle.txt')

 
'''
Triangle values are stored in the triangle.txt file.
Read each line from triangle.txt into a python list.
'''

print "The input triangle is :-"
rowlist = []
for line in f:
    print line
    row = map(int, line.split())
    rowlist.append(row)

'''
Process last two rows from the triangle and replace them by a new row
'''

while(len(rowlist) > 1):
    last_row=rowlist.pop()
    second_last_row=rowlist.pop()
    new_row = []
    for i, e in enumerate(second_last_row):
        max_element = max(last_row[i], last_row[i+1])
        new_row.append(second_last_row[i] + max_element)

    rowlist.append(new_row)

print "Total sum is : %d"%(rowlist[0][0])
print "Execution time : %s seconds" %(time.time() - start)

