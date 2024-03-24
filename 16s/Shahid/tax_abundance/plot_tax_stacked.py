import pandas as pd
import matplotlib.pyplot as plt
import sys

def plot_stacked_bar(csv_file,out_name):
    # Read the CSV file
    df = pd.read_csv(csv_file)

    # Define a dictionary to map each Bacteria Type to a specific color
    bacteria_colors = {
        'Bacteroidetes': 'orange',
        'Firmicutes': 'purple',
        'Others': 'red',
        'Proteobacteria': 'skyblue'
        # Add more Bacteria Types and colors as needed
    }

    # Transpose the DataFrame for plotting
    df_transposed = df.set_index(df.columns[0]).T

    # Plot using the custom color mapping
    ax = df_transposed.plot(kind='bar', stacked=True, figsize=(10, 6), color=[bacteria_colors.get(b, 'gray') for b in df_transposed.columns])

    # Rotate x-axis labels clockwise by 90 degrees
    ax.set_xticklabels(ax.get_xticklabels(), rotation=0, ha='right')

    # Adding labels and title
    ax.set_xlabel('DOL')
    ax.set_ylabel('Actual Abundance')

    # Customize legend
    legend = plt.legend(title='')

    # plt.show()
    plt.savefig(out_name+".pdf", format='pdf', bbox_inches='tight')
if __name__ == "__main__":
    # Check if a command-line argument is provided
    if len(sys.argv) != 3:
        print("Usage: python script_name.py <csv_file>")
        sys.exit(1)

    csv_file_name = sys.argv[1]
    outname = sys.argv[2]
    plot_stacked_bar(csv_file_name,outname)
