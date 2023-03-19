import llamahf

MODEL = 'decapoda-research/llama-7b-hf'
# MODEL = 'decapoda-research/llama-13b-hf'
# MODEL = 'decapoda-research/llama-30b-hf'
# MODEL = 'decapoda-research/llama-65b-hf'

tokenizer = llamahf.LLaMATokenizer.from_pretrained(MODEL)
model = llamahf.LLaMAForCausalLM.from_pretrained(MODEL, low_cpu_mem_usage=True)
model.to('cpu')

batch = tokenizer("The highest mountain in China is ", return_tensors="pt")
print(tokenizer.decode(model.generate(batch["input_ids"].cpu(), max_length=256)[0]))