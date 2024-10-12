def read_csv(file_path):
    with open(file_path, 'r') as file:
        return set(line.strip() for line in file)

file1_path = './outputs/threshold_0.25/datas/skin_sun_exposed_lower_leg.csv'
file2_path = './outputs/corelated_genes(g0.15)/skin_sun_exposed_lower_leg_corelated_genes.csv'

file1_data = read_csv(file1_path)
print(f"Number of values in file1: {len(file1_data)}")
file2_data = read_csv(file2_path)
print(f"Number of values in file2: {len(file2_data)}")

common_values = file1_data.intersection(file2_data)
print(f"Number of common values: {len(common_values)}")