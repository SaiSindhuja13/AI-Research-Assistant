from langchain.llms import HuggingFacePipeline
from transformers import pipeline

# Create a Hugging Face text-generation pipeline
pipe = pipeline(
    "text-generation",
    model="gpt2",  # small model for testing
    max_length=100,
    do_sample=True,
    temperature=0.7,
)

# Wrap it for LangChain
llm = HuggingFacePipeline(pipeline=pipe)

# Run prompt
response = llm("Summarize what ChatGPT is in one sentence.")

print(response)

