# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#Reading the file
data=pd.read_csv(path)

#Code starts here

# Step 1 
#Reading the file
#Creating a new variable to store the value counts
loan_status =data['Loan_Status'].value_counts(ascending=False)
#Plotting bar plot
plt.figure(figsize=[14,8])
plt.xlabel("Loan Approvals ")
plt.ylabel("No of loans")
plt.title("visualizing the company's record with respect to loan approvals")
loan_status.plot(kind="bar")
plt.show()

# Step 2
#Plotting an unstacked bar plot
property_and_loan= data.groupby(['Property_Area','Loan_Status']).size().unstack()
property_and_loan.plot(kind='bar', stacked=False, figsize=(15,10))

# Plot stacked bar chart
#Changing the x-axis label
plt.xlabel('Property Area')
#Changing the y-axis label
plt.ylabel('Loan Status')
#Rotating the ticks of X-axis
plt.xticks(rotation=45)
# Display plot
plt.show()

# Step 3
#Plotting a stacked bar plot
education_and_loan = data.groupby(['Education', 'Loan_Status']).size().unstack()
education_and_loan.plot(kind='bar', stacked=True, figsize=(15,10))

# Plot stacked bar chart
#Code starts here
#Changing the x-axis label
plt.xlabel('Education Status')

#Changing the y-axis label
plt.ylabel('Loan Status')

#Rotating the ticks of X-axis
plt.xticks(rotation=45)
# Display plot
plt.show()

# Step 4 
#Subsetting the dataframe based on 'Education' column
graduate=data[data['Education'] == 'Graduate']

#Subsetting the dataframe based on 'Education' column
not_graduate=data[data['Education'] == 'Not Graduate']

#Plotting density plot for 'Graduate'
graduate['LoanAmount'].plot(kind='density',label='Graduate')

#Plotting density plot for 'Non Graduate'
not_graduate['LoanAmount'].plot(kind='density', label='Not Graduate')

#For automatic legend display
plt.legend(labels=['Graduate', 'Not Graduate'])

# Step 5
#Setting up the subplots
fig, (ax_1,ax_2,ax_3) = plt.subplots(1,3, figsize=(20,8))

# plotting scatter plot
ax_1.scatter(data['ApplicantIncome'],data["LoanAmount"])

#Setting the subplot axis title
ax_1.set_title('Applicant Income')

#Plotting scatter plot
ax_2.scatter(data['CoapplicantIncome'],data["LoanAmount"])

#Setting the subplot axis title

ax_2.set_title('Coapplicant Income')

#Creating a new column 'TotalIncome'
data['TotalIncome']=data['ApplicantIncome'] + data['CoapplicantIncome']

#Plotting scatter plot
ax_3.scatter(data['TotalIncome'],data["LoanAmount"])




#Setting the subplot axis title
ax_3.set_title('Total Income')



