import csv

csv_filename = "extracted_data.csv"
with open(csv_filename, 'w', newline='') as file:
            csv_writer = csv.writer(file)

           
            #csv_writer.writerow(" ")