import numpy as np
#Task 1
rng = np.random.default_rng()
Cities=np.array(["Mumbai","Delhi","Chennai","Pune"])
Weather_data=np.array(rng.integers(20,40,size=(30,4)))#generating realistic random temp of cities
Final_data=np.vstack([Cities,Weather_data])
print("Temperature of Cities for 30 days:- ")
print(Final_data)
# for i in range(0,5 ):
#     Average_data=np.average(Weather_data[i])#Average of all temp cities combined for that particular day
#     print(Average_data)
Average_data=np.average(Weather_data, axis=0)#Average of all cities
print(Average_data)
#Task 2
hd=np.max(Weather_data)#hottest day overall
cd=np.min(Weather_data)#coldest day overall

#Task 3
Avg_All_Cities=np.average(Weather_data, axis=0)#average of all cities for 30 days
MaxTemp_perCity=np.max(Weather_data,axis=0)#Max temperaure that all cities have reached
MinTemp_perCity=np.min(Weather_data,axis=0)
print("Average of All CIties: ",Avg_All_Cities)
print("Max temps of all cities",MaxTemp_perCity)
print("Max temps of all cities",MinTemp_perCity)

#Task 4

print("Days when Mumbai's temp was higher than 35: ")
for i in range(0,30):
    if(Weather_data[i,0]>35):
        print("day: ",i+1)

print("Days when Pune's temp was less than 25: ")
for i in range(0,30):
    if(Weather_data[i,3]<25):
        print("day: ",i+1)
#Task 5
print("Due to heatwave, temp at all days have increases by 1.5, therfore temps are: ")
Weather_data=Weather_data+1.5
print(Weather_data)