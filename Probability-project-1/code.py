# --------------
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataframe
df = pd.read_csv(path)

#Code starts here
#Task 1
p_a=df[df['fico']>700].shape[0]/df.shape[0]
print("Probability of fico credit score greater than 700 is ",p_a)

p_b=df[df['purpose']=='debt_consolidation'].shape[0]/df.shape[0]
print("Probability of purpose equal to debt_consolidation is ",p_b)

df1=df[df['purpose']=='debt_consolidation']
# df1.head()
p_a_b=df1[df1['fico']>700].shape[0]/df1.shape[0]
print("probablityp(B|A)",p_a_b)

result= (p_a_b==p_a)
print(result)

#Task 2
prob_lp=df[df['paid.back.loan']=='Yes'].shape[0]/df.shape[0]
print(prob_lp)

prob_cs=df[df['credit.policy']=='Yes'].shape[0]/df.shape[0]
print(prob_cs)

new_df=df[df['paid.back.loan']=='Yes']
# new_df.head()

prob_pd_cs=new_df[new_df['credit.policy']=='Yes'].shape[0]/new_df.shape[0]
print(prob_pd_cs)

bayes=prob_pd_cs*prob_lp/prob_cs
print("value of bayes is",round(bayes,4))

#Task 3
pur=df['purpose'].value_counts(normalize=True)
pur.plot(kind='bar')
plt.xlabel("purpose")
plt.ylabel("P(purl)")
plt.show()

df1=df[df['paid.back.loan'] == 'No']
# df1.head()

purpl=df1['purpose'].value_counts(normalize=True)
purpl.plot(kind='bar')
plt.xlabel("purpose where paid.back.loan is No")
plt.ylabel("p(purpl)")
plt.show()

#Task 4
inst_median=df['installment'].median()
print(inst_median)

inst_mean=df['installment'].mean()
print(inst_mean)

df['installment'].hist(normed=True,bins=50)
plt.axvline(x=inst_median,color='r')
plt.axvline(x=inst_mean,color='g')
plt.xlabel("installment")
plt.ylabel("Probability")
plt.show()

df['log.annual.inc'].hist(normed=True,bins=50)
plt.xlabel("log.annual.inc")
plt.ylabel("Probability")
plt.show()




