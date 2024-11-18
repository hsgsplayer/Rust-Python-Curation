import json
from datasets import Dataset, load_dataset

raw_dataset: Dataset = load_dataset(
    "json",
    data_files="./datasets/seed5/data-sc2-1shot-i_r-ea495-1-20241112_221103.jsonl",
)

print(raw_dataset)

for content in raw_dataset['train']:
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
    break