import csv

with open("Weight.csv",newline="") as f:
    reader=csv.reader(f)
    file_data=list(reader)

file_data.pop(0)

Weight_data=[]
for i in range(len(file_data)):
    num=file_data[i][2]
    Weight_data.append(float(num))


n=len(Weight_data)

Weight_data.sort()
if (n % 2==0):
    median1=float(Weight_data[n//2])
    median2=float(Weight_data[n//2-1])
    median=((median1+median2)/2)
else:
    median=float(Weight_data[n//2])

print(median)
