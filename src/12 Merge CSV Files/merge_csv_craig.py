import csv

def merge_csv(csv_list, output_file):
    # build list with all fieldnames
    fieldnames = []
    for file in csv_list:
        with open(file, 'r', encoding='utf-8') as input_csv:
            fields = csv.DictReader(input_csv).fieldnames
            fieldnames.extend(f for f in fields if f not in fieldnames)

    # Now write a new file
    with open(output_file, "w") as output_csv:
        writer = csv.DictWriter(output_csv, fieldnames=fieldnames)
        writer.writeheader()
        for file in csv_list:
            with open(file, 'r', encoding='utf-8') as input_csv:
                reader = csv.DictReader(input_csv)
                for row in reader:
                    writer.writerow(row)



csv_list = [ 'class1.csv' , 'class2.csv' ]
output_file = 'merged.csv'
merge_csv( csv_list, output_file )