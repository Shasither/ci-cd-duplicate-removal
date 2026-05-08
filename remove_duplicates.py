
import pandas as pd
import os

# To load dataset
df = pd.read_csv('dataset.csv')

# To remove duplicates
cleaned_df = df.drop_duplicates()

# Create output folder
os.makedirs('data', exist_ok=True)

# Save cleaned dataset
cleaned_df.to_csv('data/processed_dataset.csv', index=False)

print("Duplicate removal completed successfully.")
