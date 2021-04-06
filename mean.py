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
total=0
for t in Weight_data:
    total=total+t
mean=total/n
print("mean  :"+str(mean))

