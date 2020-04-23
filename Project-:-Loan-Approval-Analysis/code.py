# --------------
# Import packages
import numpy as np
import pandas as pd
from scipy.stats import mode 
#step 1#
# code starts here
df=bank=pd.read_csv(path,sep=',', delimiter=None, header='infer',names=None,index_col=None, usecols=None)

categorical_var=bank.select_dtypes(include='object')
print(categorical_var)

numerical_var =df.select_dtypes(include='number')
print(numerical_var)

#step 2#
import numpy as np
import pandas as pd
from scipy.stats import mode

bank.drop(['Loan_ID'],axis=1, inplace=True)
banks=bank

print(banks.isnull().sum())
print(banks)
bank_mode=banks.mode()
banks= banks.replace(np.nan, bank_mode)
print(banks)
#step 3#
import pandas as pd 
avg_loan_amount=pd.pivot_table(banks,index=['Gender','Married','Self_Employed'],values='LoanAmount')
print(avg_loan_amount)

#step 4#
filt=(banks['Self_Employed'] == 'Yes')
filt1=(banks['Loan_Status'] == 'Y')
loan_approved_se=len(banks[filt & filt1])
print(loan_approved_se)

filt2=(banks['Self_Employed'] == 'No')
filt3=(banks['Loan_Status'] == 'Y')
loan_approved_nse=len(banks[filt2 & filt3])
print(loan_approved_nse)

percentage_se = (loan_approved_se * 100 / 614)
percentage_nse = (loan_approved_nse * 100 / 614)

print(percentage_se)
print(percentage_nse)

#step 5#
loan_term=banks['Loan_Amount_Term'].apply(lambda x : int(x) / 12)
print(loan_term)


big_loan_term =len(banks[loan_term >= 25])
print(big_loan_term)
#step 6#
columns_to_show = ['ApplicantIncome', 'Credit_History']
 
loan_groupby=banks.groupby(['Loan_Status'])

loan_groupby=loan_groupby[columns_to_show]

# Check the mean value 
mean_values=loan_groupby.agg([np.mean])

print(mean_values)

# code ends here


