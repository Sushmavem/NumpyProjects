import pandas as pd
import numpy as np

# Load the dataset using pandas
data = pd.read_csv('data.csv')

# Print the first few rows to verify the data
print("Dataset:")
print(data.head())

# Perform basic data analysis using pandas and numpy

# 1. Mean (Average)
mean_age = np.mean(data['Age'])
mean_height = np.mean(data['Height'])
mean_weight = np.mean(data['Weight'])

# 2. Median
median_age = np.median(data['Age'])
median_height = np.median(data['Height'])
median_weight = np.median(data['Weight'])

# 3. Standard Deviation
std_age = np.std(data['Age'])
std_height = np.std(data['Height'])
std_weight = np.std(data['Weight'])

# 4. Minimum and Maximum
min_age = np.min(data['Age'])
max_age = np.max(data['Age'])
min_height = np.min(data['Height'])
max_height = np.max(data['Height'])
min_weight = np.min(data['Weight'])
max_weight = np.max(data['Weight'])

# Print the results
print("\nBasic Data Analysis Results:")
print(f"Mean Age: {mean_age}")
print(f"Mean Height: {mean_height}")
print(f"Mean Weight: {mean_weight}")

print(f"Median Age: {median_age}")
print(f"Median Height: {median_height}")
print(f"Median Weight: {median_weight}")

print(f"Standard Deviation of Age: {std_age}")
print(f"Standard Deviation of Height: {std_height}")
print(f"Standard Deviation of Weight: {std_weight}")

print(f"Minimum Age: {min_age}, Maximum Age: {max_age}")
print(f"Minimum Height: {min_height}, Maximum Height: {max_height}")
print(f"Minimum Weight: {min_weight}, Maximum Weight: {max_weight}")
