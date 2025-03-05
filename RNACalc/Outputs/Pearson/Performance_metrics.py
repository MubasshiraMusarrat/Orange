import os
import pandas as pd
import glob
from sklearn.metrics import mean_squared_error, r2_score

# Folder containing CSV files
folder_path = "./CSVs"  

# Output file
output_file = "summary_results.csv"

# List to store results
summary_data = []

# Get all CSV files in the folder
csv_files = glob.glob(os.path.join(folder_path, "*.csv"))

for file in csv_files:
    # Extract organ name from filename
    filename = os.path.basename(file)
    organ_name = "_".join(filename.split("_")[:-1])  # Remove the last part (rnaCalc.csv)
    
    # Read the CSV file
    df = pd.read_csv(file)
    
    # Calculate RMSE and R²
    rmse = mean_squared_error(df['ChronAge'], df['RNAAge'], squared=False)
    r2 = r2_score(df['ChronAge'], df['RNAAge'])
    
    # Append to summary list
    summary_data.append([organ_name, rmse, r2])

# Create a summary DataFrame
summary_df = pd.DataFrame(summary_data, columns=['Organ', 'RMSE', 'R_Square'])

# Save to CSV
summary_df.to_csv(output_file, index=False)

print(f"Summary saved to {output_file}")
