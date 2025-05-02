import pandas as pd
from ofi_features import compute_best_level_ofi
from utils import compute_integrated_ofi


#load the csv file
df = pd.read_csv('first_25000_rows.csv')

#we have 10 depth levels
# Compute OFI for depth levels 0 to 9
ofi_levels = []  #list to store OFI series for each level

for level in range(10):  #for bid_px_00 to bid_px_09
    ofi = compute_best_level_ofi(df, level)
    ofi_levels.append(ofi)

#combine all OFI levels into a single dataFrame
multi_ofi_df = pd.concat(ofi_levels, axis=1)

#renaming columns to simpler names: ofi_00, ofi_01, etc.
multi_ofi_df.columns = [f'ofi_{i:02d}' for i in range(10)]

#compute Integrated OFI from all depth levels
integrated_ofi = compute_integrated_ofi(multi_ofi_df)
multi_ofi_df['integrated_ofi'] = integrated_ofi

#results to a CSV file
multi_ofi_df.to_csv('output_ofi_features.csv', index=False)
print("OFI computed and saved to 'output_ofi_features.csv'")
