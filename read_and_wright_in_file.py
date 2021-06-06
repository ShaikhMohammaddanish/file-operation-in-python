'''
==================
File Operations
==================
subject :- To read from student.txt for names and mark.txt for Mark1 and mark2
and create file results.txt with name and total
Student
.txt

'''

try:
    st=open("student.txt")
    st.close()
except:
    with open("student.txt", "w") as st:
        st.write("danish, kiran, bamko, rohan")

try:
    mr=open("mark.txt")
    mr.close()
except:
    with open("mark.txt", "w") as mr:
        mr.write("100, 99, 50, 50")


st=open("student.txt")
mr=open("mark.txt")
name=st.read()
name=name.split(",")
mark=mr.read()
mark=mark.split(",")

result= list(zip(name, mark))
print(result)
with open("result.txt", "w") as re:
    re.write("Each tuple of list contain name of student and his mark \n \n")
    re.write("{result}".format(result=result))
mr.close()
st.close()
