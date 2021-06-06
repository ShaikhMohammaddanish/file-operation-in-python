'''
==================
File Operations
==================
Subject :- to store alphabet capital and small letters in a file using a loop
new files should be a create alpha.txt
'''

# => Code To Save Lower Case Alphabates in File Name alpha.txt

import string

f=open("alpha.txt", "w")
f.write("=> lower case alphabates are \n\n")

for t in string.ascii_lowercase:
    f.write("{0} ".format (t))

 # Code To Save Upper Case Alphabates in File Name alpha.txt

f.write("\n\n=> Upper case alphabates are \n\n")

for t in string.ascii_uppercase:
    f.write("{0} ".format (t))

f.close()
