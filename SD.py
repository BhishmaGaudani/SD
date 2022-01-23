import csv
import math
with open("data.csv",newline="")as f:
    reader=csv.reader(f)
    file_data=list(reader)

data=file_data[0]
    

def mean(new_data):
    sum=0
    n=len(new_data)

    for i in new_data:
        sum=sum+int(i)
    mean=sum/n
    return mean
    
squared_list=[]

for i in data :
    A=(int(i)-mean(data))**2
    squared_list.append(A)

Total=0
for i in squared_list:
    Total=Total+i

n=len(data)
C=Total/(n-1)

standarddeviation = math.sqrt(C)
print(standarddeviation)








