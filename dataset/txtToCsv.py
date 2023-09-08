import os
import csv

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# print(base_dir)
input_dir = os.path.join(base_dir, 'dataset','cart_clinical_trials_txt')
print(input_dir)
output_dir = os.path.join(base_dir, 'dataset','cart_clinical_trials_csv')
print(output_dir)

os.makedirs(output_dir, exist_ok=True)

for filename in os.listdir(input_dir):
    if filename.endswith('.txt'):
        input_path = os.path.join(input_dir, filename)
        output_filename = os.path.splitext(filename)[0] + '.csv'
        output_path = os.path.join(output_dir, output_filename)

        # Read the text file and write its contents to a CSV file
        with open(input_path, 'r', encoding='utf-8') as txt_file, open(output_path, 'w', newline='', encoding='utf-8') as csv_file:
            # Assuming '|' is the delimiter in the text file, you can change it as needed.
            reader = csv.reader(txt_file, delimiter='|')
            writer = csv.writer(csv_file)
            for row in reader:
                writer.writerow(row)

print("Conversion from TXT to CSV completed.")
