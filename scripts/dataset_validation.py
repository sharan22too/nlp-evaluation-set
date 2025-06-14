from datasets import load_dataset
import pandas as pd

# Load the dataset from Hugging Face
print("⏳ Downloading dataset...")
dataset = load_dataset("emotion")

# Convert the 'train' split to a DataFrame
df = dataset["train"].to_pandas()

# Label map from ID to name
label_names = dataset["train"].features["label"].names
df["label_name"] = df["label"].apply(lambda x: label_names[x])

# Show dataset stats
print("\n✅ Total rows:", len(df))

# Show label distribution
print("\n📊 Label Distribution:")
print(df["label_name"].value_counts())

# Show a few random samples
print("\n📌 Sample rows:")
print(df[["text", "label_name"]].sample(5))

# Save the DataFrame to a CSV file
output_file = "emotion_dataset.csv"
