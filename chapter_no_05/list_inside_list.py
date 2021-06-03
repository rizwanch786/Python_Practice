# list inside list
# 2d list
matrix = [[1,2,3], [4,5,6], [7,8,9]]
# access list inside lists
for i in matrix:
    print(i)

#  access every element then we use nested for loop
for sublist in matrix:
    print (end="\n")
    for i in sublist:
        print(i, end="\t")