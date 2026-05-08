
import pandas as pd

# Load original dataset
df = pd.read_csv('dataset.csv')

# Remove duplicates
cleaned_df = df.drop_duplicates()

# Test assertion
assert cleaned_df.duplicated().sum() == 0

print("Test passed: No duplicates found.")
