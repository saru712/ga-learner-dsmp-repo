# --------------
# Importing header files
#Step 1#
import numpy as np

# Path of the file has been stored in variable called 'path'

#New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]

#Code starts here
data=np.genfromtxt(path,delimiter=",",skip_header=1)
#print("\nData: \n\n",data)
#print("\nType of data: \n\n",type(data))
census=np.concatenate((data,new_record),axis=0)
print(census)
#Step 2#
import statistics  
import math
def truncate(number, digits) -> float:
    stepper = 10.0 ** digits
    return math.trunc(stepper * number) / stepper
age=census[:,0]
print(age)
max_age=max(age)
print(max_age)
min_age=min(age)
print(min_age)
age_mean=statistics.mean(age)
print("{:.2f}".format(age_mean))
a=statistics.stdev(age)
age_std=truncate(a, 2)
print(age_std)
#Step 3#
race_0=census[census[:,2]==0]
race_1=census[census[:,2]==1]
race_2=census[census[:,2]==2]
race_3=census[census[:,2]==3]
race_4=census[census[:,2]==4]
len_0=len(race_0)
print(len_0)
len_1=len(race_1)
print(len_1)
len_2=len(race_2)
print(len_2)
len_3=len(race_3)
print(len_3)
len_4=len(race_4)
print(len_4)
minority_race=3
#Code starts here
#Step 4#
senior_citizens=census[census[:,0]>60]
working_hours_sum=senior_citizens.sum(axis=0)[6]
print(working_hours_sum)
senior_citizens_len=len(senior_citizens)
avg_working_hours=working_hours_sum/senior_citizens_len
print(round(avg_working_hours,2))
#Step 5#
import statistics 
high=census[census[:,1]>10]
low=census[census[:,1]<=10]
incomeh=high[:,7]
avg_pay_high=statistics.mean(incomeh)
print("{:.2f}".format(avg_pay_high))
incomel=low[:,7]
avg_pay_low=statistics.mean(incomel)
print("{:.2f}".format(avg_pay_low))


