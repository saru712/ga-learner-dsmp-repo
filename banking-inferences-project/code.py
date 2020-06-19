# --------------
#Importing header files
import pandas as pd
import scipy.stats as stats
import math
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.stats.weightstats import ztest
from statsmodels.stats.weightstats import ztest
from scipy.stats import chi2_contingency

import warnings

warnings.filterwarnings('ignore')
#Sample_Size
sample_size=2000

#Z_Critical Score
z_critical = stats.norm.ppf(q = 0.95)  

# Critical Value
critical_value = stats.chi2.ppf(q = 0.95, # Find the critical value for 95% confidence*
                      df = 6)   # Df = number of variable categories(in purpose) - 1


#Reading file
data=pd.read_csv(path)

#Code starts here
#task 1
data_sample =data.sample(n=sample_size,random_state=0)

sample_mean= data_sample['installment'].mean()
print("Sample mean is ",sample_mean)
installment_std= data_sample['installment'].std()
print("installment_std is ",installment_std)
margin_of_error = z_critical*(installment_std/math.sqrt(sample_size))
print("margin_of_error is",margin_of_error)
confidence_interval=(sample_mean - margin_of_error, sample_mean + margin_of_error)
print('confidence_interval = ',[round(confidence_interval[0],2),round(confidence_interval[1],2)])
true_mean = data['installment'].mean()
print('true_mean = ',round(true_mean,2))
if true_mean >= confidence_interval[0] and true_mean <= confidence_interval[1]:
    print ("true mean of installment column of data lies in the confidence interval.")
else :
    print ("true mean of installment column of data does not lies in the confidence interval")

#CLT
sample_sizes = np.array([20,50,100])
plt.figure(figsize = [10,5])
for sample_size in sample_sizes:
    lst = []
    for i in range (1000):
        data_new = data.sample(sample_size)
        lst.append(data_new['installment'].mean())
    sns.distplot(lst,hist = True, label = 'sample size {}'. format(sample_size))
    plt.legend()
#Small Business Interests
data['int.rate']=data['int.rate'].map(lambda x:str(x)[:-1])

#divide column value by 100
data['int.rate']=data['int.rate'].astype(float)/100

#Applying ztest for hypothesis
z_statistic_1,p_value_1 =ztest(x1=data[data['purpose']=='small_business']['int.rate'],value=data['int.rate'].mean(),alternative ='larger')

print(("z_statistic is:{}".format(z_statistic_1)))
print(("P_value is :{}".format(p_value_1)))

#Installment vs Loan Defaulting
z_statistic_2,p_value_2 =ztest(x1=data[data['paid.back.loan']=='No']['installment'],x2=data[data['paid.back.loan']=='Yes']['installment'])

print(("z_statistic is:{}".format(z_statistic_2)))
print(("P_value is :{}".format(p_value_2)))

#Purpose vs Loan Defaulting

yes =data[data['paid.back.loan']=='Yes']['purpose'].value_counts()
no =data[data['paid.back.loan']=='No']['purpose'].value_counts()

observed=pd.concat([yes.transpose(),no.transpose()],1,keys=['Yes','No'])

print(observed)

chi2,p,dof,ex=chi2_contingency(observed)
print("critical_value is : {}".format(critical_value))

print("chi_statistic is : {}".format(chi2))

print("p_value is : {}".format(p))






