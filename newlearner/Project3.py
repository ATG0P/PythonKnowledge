import numpy as np

#Task1
Subjects=np.array(["Student IDS","Math","Physics","Chemistry","English","Computer Science"])
rng =np.random.default_rng()
marks=np.array(rng.integers(60,101, size=(5,5)))#realistic marks assuming students are toppers
ids=np.array(rng.integers(100001,100051,size=(5,1)))#ids of students
Final_Dataset1=np.hstack([ids,marks])#stacking ids and marks
Final_Dataset=np.vstack([Subjects,Final_Dataset1])#fianl format of the data set
print(Final_Dataset1)
print("Marksheets: \n",Final_Dataset)

#taskk 2
Avgpersubject=np.average(marks,axis=0)
print("Averages per subject \n",Subjects,"\n",Avgpersubject)
Highestpersubject=np.max(marks,axis=0)
print("Highest marks per subjects : \n",Subjects,"\n",Highestpersubject)
Lowestpersubject=np.min(marks,axis=0)
print("Highest marks per subjects : \n",Subjects,"\n",Lowestpersubject)

#task 3
total=(np.sum(Final_Dataset1[:,1:],axis=1)).reshape(5,1)
averagemarks=(np.average(marks,axis=1)).reshape(5,1)
print("Sum of every subject per student: \n",total)
print("Average marks per student \n",averagemarks)
bottom5=np.sort(total,axis=0)
print(bottom5)
top5=np.sort(total,axis=0)[::-1]
print(top5)