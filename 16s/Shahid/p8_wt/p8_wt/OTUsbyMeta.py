import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import sys

otu_table = sys.argv[1]
meda_table = sys.argv[2]
out_table = sys.argv[3]
csv_file_path = meda_table
df = pd.read_csv(csv_file_path)
otu = pd.read_csv(otu_table)

# Replace 'column_name' with the actual name of the column you want to convert
column_name = '#NAME'
# Convert the column to a Python list
column_list = df[column_name].astype(str).tolist()
column_list.append("#NAME")

columns_to_drop = [col for col in otu.columns if col not in column_list]

otu.drop(columns=columns_to_drop, inplace=True)
sorted_columns = otu.columns
# Create a new DataFrame with the sorted columns
otu = otu[sorted_columns]

otu.to_csv(out_table, index=False)