from datasets import load_dataset
# specific language (e.g. Dockerfiles)
dataset = load_dataset("bigcode/the-stack-dedup", data_dir="data/python", streaming=True, split="train")
for example in iter(dataset):
    print(example["content"])