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
first_15 = data.head(15)
data = first_15[::-1]
# data = data.head(15)
# Plot a horizontal bar chart
plt.figure(figsize=(8, 5))
plt.barh(data['Names'], data['MeanDecreaseAccuracy'])
plt.xlabel('MeanDecreaseAccuracy')
plt.ylabel('Bacteria (genus)')
plt.title('Importance')
plt.subplots_adjust(left=0.4) 
output_file_name = file_name.replace('.csv', '.pdf')
plt.savefig(output_file_name)

# Show the plot
plt.show()