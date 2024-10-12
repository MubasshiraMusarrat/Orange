import pandas as pd
import numpy as np

def convert_age_range_to_midpoint(age_range):
    if isinstance(age_range, str) and '-' in age_range:
        start, end = map(int, age_range.split('-'))
        return (start + end) / 2
    else:
        return np.nan

counts_df = pd.read_csv('./TPM_dataCSV/gene_tpm_2017-06-05_v8_skin_sun_exposed_lower_leg.csv')
counts_df = counts_df.drop(columns=['id', 'Description']).set_index('Name')
counts_df = counts_df.T
counts_df['SUBJID'] = counts_df.index.str.split('-').str[0]+'-'+counts_df.index.str.split('-').str[1]
counts_df = counts_df.set_index('SUBJID')
metadata = pd.read_csv('GTEx_Analysis_v8_Annotations_SubjectPhenotypesDS.txt', sep='\t').set_index('SUBJID')
metadata = metadata.loc[metadata.index.intersection(counts_df.index)]
samples_to_keep = ~metadata.AGE.isna()
counts_df = counts_df.loc[samples_to_keep]
metadata = metadata.loc[samples_to_keep]
metadata['AGE'] = metadata['AGE'].apply(convert_age_range_to_midpoint)
counts_df = counts_df.loc[:, (counts_df != counts_df.iloc[0]).any()]
counts_df = counts_df.fillna(counts_df.mean())
correlations = counts_df.corrwith(metadata['AGE'])
filtered_columns = correlations[correlations > 0.15].index
pd.DataFrame(filtered_columns).to_csv('./outputs/corelated_genes(g0.15)/skin_sun_exposed_lower_leg_corelated_genes.csv', index=False)
print(filtered_columns.size)