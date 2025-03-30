import json
import os
from datasets import load_dataset

# Create the data directory if it doesn't exist
os.makedirs("data", exist_ok=True)

# Process the cyber-forget-corpus dataset
forget_ds = load_dataset("cais/wmdp-corpora", "cyber-forget-corpus")
forget_split = forget_ds["train"]

with open("data/cyber-forget-corpus.jsonl", "w") as f:
    for example in forget_split:
        json_record = json.dumps(example)
        f.write(json_record + "\n")

# Process the cyber-retain-corpus dataset
retain_ds = load_dataset("cais/wmdp-corpora", "cyber-retain-corpus")
retain_split = retain_ds["train"]

with open("data/cyber-retain-corpus.jsonl", "w") as f:
    for example in retain_split:
        json_record = json.dumps(example)
        f.write(json_record + "\n")

