#OK
import pdb

def find(list1,num):
    for each in list1:
        if(each!=num):
            print(each)
        else:
            break

t=[]
for i in range(100000):
    t.append(i)

find(t,99999)
