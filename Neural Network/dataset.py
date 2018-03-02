import numpy as np

data = np.random.random((200, 2))
data = data*100

ds = []
for x in data:
    x = list(x)
    if x[0]<=40 and x[1]<=40:
        x.append('1.0')
        ds.append(x)
    elif x[0]>=60 and x[1]>=60:
        x.append('0.0')
        ds.append(x)

fp = open('owndata.txt', "w")
for x in ds:
    fp.write(str(round(x[0], 3))+'\t'+str(round(x[1], 3))+'\t'+ str(x[2]) +'\n')
fp.close()
