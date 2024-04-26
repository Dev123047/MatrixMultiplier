row1 = int(input("Enter no. of rows in matrix 1 : "))
col1 = int(input("Enter no. of columns in matrix 1 : "))
row2 = int(input("Enter no. of rows in matrix 2 : "))
col2 = int(input("Enter no. of columns in matrix 2 : "))
#declaring variables for the two matrices to be multiplied and the final resultant matrix
m1 = []         #multiplicant 1 matrix
m2 = []         #multiplicant 2 matrix
m = []          #resultant matrix
#making matrix 1 placeholder
for a in range(row1):
    m1.append([])           #creating the placeholder nested list for rows in matrix 1
for b in range(len(m1)):
    for c in range(col1):
        m1[b].append(0)     #creating the placeholder values(0) for elements of matrix 1
#making matrix 2 placehoder
for d in range(row2):
    m2.append([])           #creating the placeholder nested list for rows in matrix 1
for e in range(len(m2)):
    for f in range(col2):
        m2[e].append(0)     #creating the placeholder values (0) for elements of matrix 1
#input matrix 1
for g in range(row1):
    for h in range(col1):
        num = int(input("Enter element at Row {} and Column {} of Matrix 1: ".format(g+1,h+1)))
        m1[g][h] += num
#input matrix 2
for i in range(row2):
    for j in range(col2):
        num = int(input("Enter element at Row {} and Column {} of Matrix 2: ".format(i+1,j+1)))
        m2[i][j] += num
#making final matrix placeholder
for k in range(row1):
    m.append([])
for l in range(row1):
    for d in range(col2):
        m[l].append(0)
#multiplying
for p in range(row1):
    for n in range(col2):
        for o in range(col1):
            m[p][n] += m1[p][o]*m2[o][n]
#printing final result
for q in range(len(m)):
    for r in range(len(m[q])):
        print(m[q][r],end="\t")
    print()