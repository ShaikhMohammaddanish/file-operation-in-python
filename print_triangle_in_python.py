'''
==================
File Operations
==================

subject :- save a triangle with * for a given number of line (baswcially create regular triangle in a file)

'''
g= int(input("Enter nuber of row of triangle"))
if g<=2:
    print("enter value higher thern Two")
else:
    l=open("triangle.txt", "w")
    ls = list(range(1, g+1))
    for y in ls:
        # y=(y*2)-1
        l.write("{: ^{k}}\n".format("* "*y, k=2*len(ls)))
    l.close()
