import csv

tsv_file = 'path_abun_unstrat_descrip.tsv'  # Path to the input TSV file
csv_file = 'path_abun_unstrat_descrip.csv'  # Path to the output CSV file

# Open the TSV file for reading and the CSV file for writing
with open(tsv_file, 'r', newline='', encoding='utf-8') as tsvfile, open(csv_file, 'w', newline='', encoding='utf-8') as csvfile:
    tsv_reader = csv.reader(tsvfile, delimiter='\t')  # Create a TSV reader
    csv_writer = csv.writer(csvfile)  # Create a CSV writer

    # Iterate over each row in the TSV file
    for row in tsv_reader:
        csv_writer.writerow(row)  # Write the row to the CSV file

print('Conversion complete.')
