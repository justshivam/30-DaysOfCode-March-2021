import numpy as np
def conv(n):
    return int(n)
userin=input()
arr= np.array(list(map(conv,userin)))
indx= list(range(1,len(arr)+1))
raw= arr**indx
if raw.sum() == int(userin):
    print(userin,"Is a disarium")
else:
    print(userin,"Is not a disarium")
