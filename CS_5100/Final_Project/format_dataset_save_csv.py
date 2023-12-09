import csv
from datasets import load_dataset

def extract_comment_code_pairs(content):
    lines = content.split('\n')

    comment_code_pairs = []
    current_comment = ""
    current_code = ""
    capture_code = False

    for line in lines:
        line = line.strip()
        if line.startswith('#'):  # Start of a new comment
            if current_comment and current_code:
                comment_code_pairs.append((current_comment, current_code))
                current_code = ""
            current_comment = line[1:].strip()  # Remove '#' and leading whitespace
            capture_code = True
        elif capture_code:
            if line:  # Non-empty line, considered as code
                current_code += line + '\n'
            else:  # Empty line, end of the current code block
                capture_code = False
                if current_comment and current_code:
                    comment_code_pairs.append((current_comment, current_code))
                    current_code = ""

    # Adding the last pair if exists
    if current_comment and current_code:
        comment_code_pairs.append((current_comment, current_code))

    return comment_code_pairs

# Load your dataset
dataset = load_dataset("bigcode/the-stack-dedup", data_dir="data/python", streaming=True, split="train")

# Prepare a file to save the pairs
output_file = 'comment_code_pairs.csv'
with open(output_file, 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Comment', 'Code'])  # Writing header

    # Iterate through the dataset and process each example
    for example in iter(dataset):
        content = example["content"]
        pairs = extract_comment_code_pairs(content)
        print("written")
        for comment, code in pairs:
            writer.writerow([comment, code.replace('\n', '\\n')])  # Write each pair to the file

print(f"Comment-code pairs have been saved to {output_file}")
