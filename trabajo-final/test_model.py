import joblib
import numpy as np

# Load the MLP model and PCA transformer
model_path = "models/mlp.pkl"  # Path to your MLP model
pca_path = "models/pca.pkl"    # Path to your PCA transformer
mlp_model = joblib.load(model_path)
pca_transformer = joblib.load(pca_path)

# Input dataset parameters (replace with your actual feature values)
# Ensure features are in the original input format
import pandas as pd

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
ds_path = "data/marketing_campaign.csv"
df = pd.read_csv(ds_path, delimiter="\t")


df.head(1)