import random
from datasets import load_dataset
from pathlib import Path

import logging


import os
import time
import math
from transformers import AutoTokenizer, BertTokenizer, RobertaTokenizer, T5Tokenizer, TFT5ForConditionalGeneration, create_optimizer
import random
import datetime
import transformers.integrations
from pathlib import Path
from transformers import TFGenerationMixin
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "1"  # reduce the amount of console output from TF
import tensorflow as tf
import transformers
from datasets import load_dataset
#logging.set_verbosity_warning()
#logging.set_verbosity_error()


class Args:
    # define training arguments
    
    # MODEL
    model_type = 't5'
    tokenizer_name = 'Salesforce/codet5-base'
    model_name_or_path = 'Salesforce/codet5-base'
    
    # DATA
    train_batch_size = 8 # memory issue at 8
    validation_batch_size = 8  # memory issue at 8
    max_input_length = 48 # originally 48
    max_target_length = 128 # originally 128
    prefix = "Generate Python: "    

    # OPTIMIZER
    learning_rate = 3e-4
    weight_decay = 1e-4
    warmup_ratio = 0.2
    adam_epsilon = 1e-8

    # TRAINING
    seed = 2022
    epochs = 20

    # DIRECTORIES
    output_dir = "runs/"
    logging_dir = f"{output_dir}/logs/"
    checkpoint_dir = f"checkpoint"
    save_dir = f"{output_dir}/saved_model/"
    cache_dir = f"{output_dir}/working/"
  #  cache_dir = '../working/'
    Path(output_dir).mkdir(parents=True, exist_ok=True)
    Path(logging_dir).mkdir(parents=True, exist_ok=True)
    Path(save_dir).mkdir(parents=True, exist_ok=True)
    

args = Args()

def run_predict(args, text):
    # load saved finetuned model
    model = TFT5ForConditionalGeneration.from_pretrained(args.save_dir)
    # load saved tokenizer
    tokenizer = RobertaTokenizer.from_pretrained(args.save_dir) 
    
     # encode texts by prepending the task for input sequence and appending the test sequence
    query = args.prefix + text 
    encoded_text = tokenizer(query, return_tensors='tf', padding='max_length', truncation=True, max_length=args.max_input_length)
    
    # inference
    generated_code = model.generate(
        encoded_text["input_ids"], attention_mask=encoded_text["attention_mask"], 
        max_length=args.max_target_length, top_p=0.95, top_k=50, repetition_penalty=2.0, num_return_sequences=1
    )
    
    # decode generated tokens
    decoded_code = tokenizer.decode(generated_code.numpy()[0], skip_special_tokens=True)
    return decoded_code

def predict_from_dataset(args):
    # load using hf datasets
    dataset = load_dataset('json', data_files='working/mbpp.jsonl') 
    # train test split
    dataset = dataset['train'].train_test_split(0.1, shuffle=False) 
    test_dataset = dataset['test']
    
    # randomly select an index from the validation dataset
    index = random.randint(0, len(test_dataset))
    text = test_dataset[index]['text']
    code = test_dataset[index]['code']
    
    # run-predict on text
    decoded_code = run_predict(args, text)
    
    print("#" * 25); print("QUERY: ", text); 
    print()
    print('#' * 25); print("ORIGINAL: "); print("\n", code);
    print()
    print('#' * 25); print("GENERATED: "); print("\n", decoded_code);
    
def predict_from_text(args, text):
    # run-predict on text
    decoded_code = run_predict(args, text)
    print("#" * 25); print("QUERY: ", text); 
    print()
    print('#' * 25); print("GENERATED: "); print("\n", decoded_code);





# example 1
predict_from_dataset(args)
# example 2
predict_from_dataset(args)
# example 3
predict_from_dataset(args)





predict_from_text(args, "Write a function to print hello world"); print()
# example 1
predict_from_text(args, "Write a function to add two random numbers"); print()
# example 2
predict_from_text(args, "Write a function to find the frequency of items in a list"); print()
# example 3
predict_from_text(args, "Write a function to concatenate two dictionary"); print()

