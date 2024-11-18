import json
from datasets import Dataset, load_dataset

raw_dataset: Dataset = load_dataset(
    "json",
    data_files="./datasets_rust/seed5/data-sc2-1shot-i_r-8600d-1-20241114_020603.jsonl",
)

print(raw_dataset)

content = raw_dataset['train'][100]
print(
    "@@@Seed",
    content['seed'],
    "@@@Instruction",
    content['instruction'],
    "@@@Response",
    content['response'],
    sep="\n",
    end="\n\n",
)