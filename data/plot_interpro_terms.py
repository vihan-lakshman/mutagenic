import pandas as pd
import matplotlib.pyplot as plt
merged_final = pd.read_csv('prelim-deletion-validation-dataset-functional-annotations-with-interpro.csv')
merged_final['num_interpro'] = merged_final['InterPro'].fillna('').str.split(';').apply(len)
merged_final['num_interpro'] = merged_final['num_interpro']-1
merged_final['num_interpro'].hist()
plt.xlabel('Number of interpro terms')
plt.title('How many interpro terms are there for each sequence?')
plt.ylabel('Count')