import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


kfshrc_Project = pd.read_csv('Healthcare Delivery Indictors  Corporate Level 2022.csv')
kfshrc_Project

kfshrc_Project.info()

kfshrc_Project[['INDICATORS','Value']].describe().round(2)

kfshrc_Project['INDICATORS'].unique()

kfshrc_Project['INDICATORS'].nunique()

kfshrc_Project['INDICATORS'].value_counts()

kfshrc_Project['Value'].value_counts()

kfshrc_Project.isna().sum()

kfshrc_Project.duplicated().sum(
    
kfshrc_Project.sample(10)

kfshrc_Project['INDICATORS'].value_counts().plot.bar()

top_10_max_values = kfshrc_Project.nlargest(10, 'Value')
print(top_10_max_values
      
bottom_10_min_values = kfshrc_Project.nsmallest(10, 'Value')
print(bottom_10_min_values)


selected_categories = ['Inpatient Days', 'Outpatient Visits', 'Total Surgeries','Bed Occupancy Rate (%)']

filtered_rows = kfshrc_Project[kfshrc_Project['INDICATORS'].isin(selected_categories)]

print(filtered_rows)

selected_metrics = ['Number of Admitted Patients', 'Number of ICU Beds', 'Department of Emergency Medicine (DEM) Visits']

selected_rows = kfshrc_Project[kfshrc_Project['INDICATORS'].isin(selected_metrics)]

print(selected_rows)

selected_metrics = ['Home Renal Dialysis Visits', 'Mechanically Ventilated Patients', 'Other HHC Visits']

selected_rows = kfshrc_Project[kfshrc_Project['INDICATORS'].isin(selected_metrics)]

print(selected_rows)

kfshrc_Project.to_csv('kfshrc_Project-expansion-kfshrc.csv')
