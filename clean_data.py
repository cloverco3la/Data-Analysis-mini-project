
from calendar import month

from matplotlib import markers
import pandas as pd
import kagglehub
import os

# Step 1: Download dataset
path = kagglehub.dataset_download(
    "vivek468/superstore-dataset-final"
)

# Step 2: Check available files
#print(os.listdir(path))

# Step 3: Load dataset

file_path = os.path.join(path, "Sample - Superstore.csv")

df = pd.read_csv(file_path, encoding="latin1")
df["Order Date"] = pd.to_datetime(df["Order Date"], format="%m/%d/%Y")
df["Ship Date"] = pd.to_datetime(df["Ship Date"], format="%m/%d/%Y")

print(df.head(10))
# print(df.shape)
# print(df.info())
# print(df.isnull().sum())
# print(df.duplicated().sum())

