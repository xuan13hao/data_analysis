import sys
import pandas as pd
import matplotlib.pyplot as plt

# Get the file name from the terminal
if len(sys.argv) == 2:
    file_name = sys.argv[1]
else:
    print("Please provide the file name as a command-line argument.")
    sys.exit()

# Read the CSV file
data = pd.read_csv(file_name)
# Filter out rows where Pvalues > 0.05 and abs(LDAscore) < 2
filtered_data = data[(data['Pvalues'] <= 0.05) & (abs(data['LDAscore']) >= 2)]

# Create a new column with absolute values of LDAscore
filtered_data['Abs_LDAscore'] = abs(filtered_data['LDAscore'])

# Sort the filtered data by absolute value of LDAscore in descending order
sorted_data = filtered_data.sort_values('Abs_LDAscore', ascending=False).head(15)

sorted_data = sorted_data.sort_values('LDAscore', ascending=False)

sorted_data = sorted_data[::-1]
# Plot a horizontal bar chart
plt.figure(figsize=(10, 10))
plt.barh(sorted_data['Names'], sorted_data['LDAscore'])
plt.xlabel('LDAscore')
plt.ylabel('Bacteria (genus)')
plt.subplots_adjust(left=0.4) 
output_file_name = file_name.replace('.csv', '.pdf')
plt.savefig(output_file_name)
# Show the plot
plt.show()