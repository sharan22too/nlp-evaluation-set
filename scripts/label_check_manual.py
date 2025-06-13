from datasets import load_dataset
import pandas as pd

# Load dataset and prepare label names
dataset = load_dataset("emotion")
df = dataset["train"].to_pandas()
label_names = dataset["train"].features["label"].names
df["label_name"] = df["label"].apply(lambda x: label_names[x])

# Sample 20 entries for manual review
sample = df[["text", "label_name"]].sample(20, random_state=42)

# Save to file for easy review
sample.to_csv("../reports/manual_label_check.csv", index=False)
print("✅ Sample exported to: reports/manual_label_check.csv")
