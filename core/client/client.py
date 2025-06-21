import langchain

from langchain_groq.chat_models import ChatGroq

model= ChatGroq(
    model_name="groq/llama-3.1-70b-chat",
    max_retries=3,
    max_tokens=4096,
    temperature=0.1,
    top_p=0.9,)

model.invoke(
    "What is the capital of France? Please answer in one sentence.",
)

# langchain.llms.Groq is deprecated, use langchain_groq.chat_models.ChatGroq instead
# model = langchain.llms.Groq(
#     model_name="groq/llama-3.1-70b-chat",        
#     max_retries=3,
#     max_tokens=4096,
#     temperature=0.1,
#     top_p=0.9,
# )
# model.invoke(
#     "What is the capital of France? Please answer in one sentence.",
# )