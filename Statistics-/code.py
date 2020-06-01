# --------------
#Header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#Reading of the file
data=pd.read_csv(path)

# Code starts here
data['Gender'].replace('-','Agender',inplace=True)
gender_count=data['Gender'].value_counts()

#distribution of gender
gender_count.plot(kind='bar')
plt.xlabel('Gender')
plt.ylabel('No of people with gender')
plt.show()

#check does good overpower evil or does evil overwhelm good
alin_count=data['Alignment'].value_counts()
print(alin_count)
plt.figure(figsize=(6,8))
explode = (0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, .01)
labels = ['good', 'bad', 'neutral']
plt.pie(alin_count, labels=labels, autopct='%1.1f%%', shadow=True, startangle=140)
plt.title("Character Alignment")

#Check out if combat relate to person's strength or it's intelligence
sc_df=data[['Strength','Combat']].copy()
sc_covariance = sc_df['Strength'].cov(sc_df['Combat'])

print(sc_covariance)

std_strength= sc_df['Strength'].std()
print(std_strength)

std_combat=sc_df['Combat'].std()
print(std_combat)

pearson_sc = (sc_covariance/(std_strength*std_combat))
print("Pearson's coefficient for Strength and Combat is",np.round(pearson_sc,2))

ic_df=data[['Intelligence','Combat']].copy()
ic_covariance = ic_df['Intelligence'].cov(ic_df['Combat'])

print(ic_covariance)

std_intelligence= ic_df['Intelligence'].std()
print(std_intelligence)

std_combati=ic_df['Combat'].std()
print(std_combati)

pearson_ic = (ic_covariance/(std_intelligence*std_combati))
print("Pearson's coefficient for Intelligence and Combat is",np.round(pearson_ic,2))

#Find out who are the best of the best in this superhero universe
total_high = data['Total'].quantile(q=0.99)
print(total_high)
super_best =data[data['Total']>total_high]
# print(super_best)

super_best_list =list(super_best['Name'])
super_best_names =super_best_list
print("These are the best of the best in the superhero universe",super_best_names)



