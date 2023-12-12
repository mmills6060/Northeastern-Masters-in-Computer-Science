from datasets import load_dataset

# Load "small" (or "medium", "full") function level training set
dataset = load_dataset("Fsoft-AIC/the-vault-function", split_set=["train/small"], languages=['Python'])