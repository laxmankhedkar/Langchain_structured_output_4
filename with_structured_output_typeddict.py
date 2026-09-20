# 1. Close 


# from langchain_openai import ChatOpenAI

# from typing import TypedDict
# from dotenv import load_dotenv

# load_dotenv()

# model = InferenceClient()

# class Review(TypedDict):
#     summary: str
#     sentiment : str 

# structured_model = model.with_structured_output(Review)


# result = model.structured_model.invoke('The hardware is good but the softwear not good')

# print(result)







 










from typing import TypedDict
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
import os

load_dotenv()

print(os.getenv("HF_TOKEN"))


class Review(TypedDict):
    summary: str
    sentiment: str


llm = HuggingFaceEndpoint(
    repo_id="Qwen/Qwen2.5-0.5B-Instruct",
    task="text-generation",
    max_new_tokens=100,
    temperature=0
)

model = ChatHuggingFace(llm=llm)

structured_model = model.with_structured_output(Review)

result = structured_model.invoke(
    "The hardware is good but the software is not good."
)

print(result)