import os
import csv

data_dir = os.path.dirname(os.path.abspath(__file__))

# Directory where the CSV files are stored
csv_folder = os.path.join(data_dir, 'cart_clinical_trials_csv')

# README.md file to write attributes
readme_file = os.path.join(data_dir, 'README.md')

# Open the README.md file in write mode
with open(readme_file, "w", encoding="utf-8") as readme:
    readme.write("# Documentation on Dataset\n\n")
    for filename in os.listdir(csv_folder):
        if filename.endswith('.csv'):
            readme.write(f"## File Name: {filename}\n")

            # Extract and writew the attributes to README.md
            with open(os.path.join(csv_folder, filename), "r", encoding="utf-8") as csv_file:
                reader = csv.reader(csv_file)
                header = next(reader)
                readme.write("<b>Attributes:</b><br>\n")
                for attribute in header:
                    readme.write(f"- {attribute}<br>\n")
                
            readme.write("\n")
            
