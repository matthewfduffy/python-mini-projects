import CSV

csv_file_name = "path/to/file.csv"

csv_reader_dict = csv.DictReader(open(csv_file_name,  mode='r'))

for csv_row in csv_reader_dict:
    print(f'{csv_row["your_csv_header_1"]}')