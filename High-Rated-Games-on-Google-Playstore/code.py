# --------------
#Importing header files
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import MinMaxScaler, LabelEncoder


#Loading the data
data=pd.read_csv(path)
#plot histogram of Rating
s = data['Rating']
fig, ax = plt.subplots()
ax.hist(s.dropna(), alpha=0.9, color='blue')
plt.show()
# Plot histogram of Rating>5
data_rating =data[data['Rating'] <= 5]
data_rating.plot(kind='hist')
plt.show()

# ploting boxplot between category and rating 
plt.figure(figsize=(8,8))
cat =sns.catplot(x='Category',y='Rating',data=data,kind="box",height=10)
cat.set_xticklabels(rotation=90)
plt.title("Rating vs Category Boxplot",size=20)
plt.show()

# missing values 
mean_rating = data['Rating'].mean(skipna=True)
print (mean_rating)

data['Rating'] = data.Rating.fillna(mean_rating) 
print (data['Rating'])

data['Type']=data['Type'].fillna(method ='ffill')

data['Content Rating']=data['Content Rating'].fillna(method ='ffill')

data['Current Ver']=data['Current Ver'].fillna(method ='ffill')
data['Android Ver']=data['Android Ver'].fillna(method ='ffill')

total_null= data.isnull().sum()
print(total_null)

percent_null = data.isnull().sum()*100.0/len(data)
missing_data =pd.concat([total_null,percent_null],axis=1,keys=['Total','Percent'])

print(missing_data)


#Code starts here















