import json
from datasets import load_dataset
import os

# Create the data directory if it doesn't exist
os.makedirs("data", exist_ok=True)

# Load your dataset
ds = load_dataset("cais/wmdp-corpora", "cyber-forget-corpus")

# Assuming you want to export the 'train' split
train_split = ds["train"]

# Write each example as a JSON object on its own line in data/cyber-forget-corpus.jsonl
with open("data/cyber-forget-corpus.jsonl", "w") as f:
    for example in train_split:
        json_record = json.dumps(example)
        f.write(json_record + "\n")

