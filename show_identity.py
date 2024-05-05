import pandas as pd
import matplotlib.pyplot as plt

# Read the three files
file1 = 'rawsubreads.summary_identity_stats.csv'
file1 = 'sim.summary_identity_stats.csv'

# Assuming the files have headers and are comma-separated
df1 = pd.read_csv(file1)

# Transpose the dataframes
df1 = df1.T

# Assuming the filenames correspond to the names you want to use for the columns
filename1 = file1.split('.')[0]  # Extracting the filename without extension

# Renaming columns to the filenames
df1.columns = [f"{filename1}_{col}" for col in df1.columns]

# Concatenate the dataframes along the columns
result = df1
#pd.concat([df1, df2], axis=1)

pd.set_option('display.float_format', lambda x: '%.3f' % x)  # Set the number of decimal places you prefer

# Display the table
print(result)
