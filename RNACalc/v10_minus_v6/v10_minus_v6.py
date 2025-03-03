import os
import pandas as pd

# Define file paths
parent_folder = os.path.abspath(os.path.join("v10_minus_v6", os.pardir))
count_data_folder = os.path.join(parent_folder, "Count_dataCSV")
v10_folder = os.path.join(parent_folder, "v10_minus_v6")
csvs_folder = os.path.join(v10_folder, "CSVs")

# Ensure CSVs folder exists
os.makedirs(csvs_folder, exist_ok=True)

# Read the main CSV file to get columns to remove
main_csv_path = os.path.join(v10_folder, "GTEx_Analysis_v6_RNA-seq_RNA-SeQCv1.1.8_gene_reads.csv")
main_df = pd.read_csv(main_csv_path)
columns_to_remove = set(main_df.columns) - {"Name", "Description"}

# Process each CSV in Count_dataCSV
for file in os.listdir(count_data_folder):
    if file.endswith(".csv"):
        file_path = os.path.join(count_data_folder, file)
        df = pd.read_csv(file_path)
        
        # Drop matching columns
        df = df.drop(columns=[col for col in df.columns if col in columns_to_remove], errors='ignore')
        
        # Modify filename
        new_file_name = file.replace("gene_reads_v10_", "gene_reads_v10_minus_v6_")
        new_file_path = os.path.join(csvs_folder, new_file_name)
        
        # Save the modified file
        df.to_csv(new_file_path, index=False)
        print(f"Processed and saved: {new_file_path}")
