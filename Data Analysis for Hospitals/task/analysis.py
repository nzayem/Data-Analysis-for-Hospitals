import pandas as pd
import matplotlib.pyplot as plt


pd.set_option('display.max_columns', 8)

general = pd.read_csv('test/general.csv')
prenatal = pd.read_csv('test/prenatal.csv')
sports = pd.read_csv('test/sports.csv')

prenatal.columns = general.columns.values
sports.columns = general.columns.values

# Concatenating the 3 dataframes
merged_data = pd.concat([general, prenatal, sports], ignore_index=True)

# Removing the row Unnamed: 0
merged_data.drop(columns='Unnamed: 0', inplace=True)

# print(merged_data.sample(n=20, random_state=30))

# Delete empty rows:
merged_data.dropna(how="all", inplace=True)

# replace the gender column:

merged_data['gender'].replace({'female': 'f', 'woman': 'f', 'male': 'm', 'man': 'm'}, inplace=True)

# Replace the NaN values in the gender column of the prenatal hospital with f

merged_data['gender'].fillna('f', inplace=True)

# Replace NaN values in the bmi, diagnosis, blood_test, ecg, ultrasound, mri, xray, children, months columns with zeros

columns_to_modify = ['bmi', 'diagnosis', 'blood_test', 'ecg', 'ultrasound', 'mri', 'xray', 'children', 'months']

merged_data[columns_to_modify] = merged_data[columns_to_modify].fillna(0, axis=0)

# Print shape of the resulting data frame

# print(merged_data.shape)

# Print random 20 rows of the resulting data frame. For the reproducible output set random_state=30

# print(merged_data.sample(n=20, random_state=30))

# 1- Which hospital has the highest number of patients?

# print(f"The answer to the 1st question is {merged_data['hospital'].value_counts().idxmax()}")
#
# # 2- What share of the patients in the general hospital suffers from stomach-related issues?
#
# total_general = merged_data.loc[(merged_data['hospital'] == 'general')].shape[0]
#
# number_stomach = merged_data.loc[(merged_data['hospital'] == 'general')
#                                  & (merged_data['diagnosis'] == 'stomach')].shape[0]
#
# share_stomach = number_stomach / total_general
#
# print(f"The answer to the 2nd question is {round(share_stomach, 3)}")
#
# # 3- What share of the patients in the sports hospital suffers from dislocation-related issues?
#
# total_sports = merged_data.loc[(merged_data['hospital'] == 'sports')].shape[0]
#
# number_dislocation = merged_data.loc[(merged_data['hospital'] == 'sports')
#                                      & (merged_data['diagnosis'] == 'dislocation')].shape[0]
#
# share_dislocation = number_dislocation / total_sports
#
# print(f"The answer to the 3rd question is {round(share_dislocation, 3)}")
#
# # 4- What is the difference in the median ages of the patients in the general and sports hospitals?
#
# median_ages = merged_data.pivot_table(index='hospital', values='age', aggfunc='median')
#
# difference_ages = int(median_ages.loc['general', 'age'] - median_ages.loc['sports', 'age'])
#
# print(f"The answer to the 4th question is {difference_ages}")
#
# # 5- In which hospital the blood test was taken the most often? How many blood tests were taken?
#
# blood_tests = merged_data.pivot_table(index='blood_test', columns='hospital', values='gender', aggfunc='count')
#
# highest_tests = int(blood_tests.max().max())
#
# hospital_highest = blood_tests.idxmax(axis=1).loc['t']
#
# print(f"The answer to the 5th question is {hospital_highest}, {highest_tests} blood tests")

# Stage 5:

# What is the most common age of a patient among all hospitals?
# Plot a histogram and choose one of the following age ranges: 0-15, 15-35, 35-55, 55-70, or 70-80

age_ranges = [0, 15, 35, 55, 70, 80]

plt.figure(1)

plt.hist(merged_data['age'], color='orange', bins=age_ranges, edgecolor='white')

# What is the most common diagnosis among patients in all hospitals? Create a pie chart ?

# https://stackoverflow.com/questions/69024302/matplotlib-pie-chart-label-does-not-match-value
# This is needed to match the labels with the values in the Chart

count_diagnosis = merged_data.diagnosis.value_counts()

Labels_diagnosis = count_diagnosis.index

plt.figure(2)

plt.pie(count_diagnosis, labels=Labels_diagnosis, autopct='%.1f%%')

# Build a violin plot of height distribution by hospitals. Try to answer the questions:
# What is the main reason for the gap in values?
# Why there are two peaks, which correspond to the relatively small and big values?
# No special form is required to answer this question

plt.figure(3)

plt.violinplot(merged_data['height'])

print("The answer to the 1st question: 15-35")
print("The answer to the 2nd question: pregnancy")
print("The answer to the 3rd question: It's because the difference of ages, small values corresponds to infants"
      "and the large values are for adults")

plt.show()
