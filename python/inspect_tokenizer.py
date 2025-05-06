from transformers import AutoTokenizer
import torch
#colab 
tokenizer = AutoTokenizer.from_pretrained("gpt2")

# Sample input text
sample_text = "Look, if you had one shot or one opportunity..."
tokens = tokenizer(sample_text, return_tensors="pt", padding=True, truncation=True)

print("Token IDs:", tokens["input_ids"])
print("Shape:", tokens["input_ids"].shape)

print("\n Attention Mask:", tokens["attention_mask"])
