from transformers import pipeline
import pandas as pd

df = pd.read_csv("day4_rule_based_nlp_testcases.csv")
from transformers import pipeline
classifier = pipeline("text-classification", model="j-hartmann/emotion-english-distilroberta-base", top_k=1)

df['model_prediction'] = df['text'].apply(lambda x: classifier(x)[0]['label'].lower())
df['match'] = df['model_prediction'] == df['expected_label']

accuracy = df['match'].mean()
print(f"Accuracy: {accuracy:.2%}")

mismatches = df[df['match'] == False][['text', 'expected_label', 'model_prediction']]
print("Mismatches:")
print(mismatches.to_string(index=False))
