pip install transformers torch pandas

import torch
from transformers import GPT2LMHeadModel, GPT2Tokenizer

# Load pre-trained model and tokenizer from Hugging Face
model_name = "gpt2"  # GPT-2 model

tokenizer = GPT2Tokenizer.from_pretrained(model_name)
model = GPT2LMHeadModel.from_pretrained(model_name)

# Input prompt for text generation
prompt = "In a distant future, humanity will"

# Tokenize the input prompt
input_ids = tokenizer.encode(prompt, return_tensors="pt")

# Generate text (set the max length to control how much text is generated)
output = model.generate(input_ids, max_length=100, num_return_sequences=1, no_repeat_ngram_size=2, temperature=0.7, top_k=50)

# Decode the output tokens back into human-readable text
generated_text = tokenizer.decode(output[0], skip_special_tokens=True)

print(generated_text)
