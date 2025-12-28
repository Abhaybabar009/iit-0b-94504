from langchain_groq import ChatGroq
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_openai import ChatOpenAI
import os

from langchain.chat_models import init_chat_model
from dotenv import load_dotenv
load_dotenv()

api_key=os.getenv("GEMINI_API_KEY")
llm = ChatGoogleGenerativeAI(
    model = "gemini-2.5-flash",
    api_key = api_key
)


user_input = input("You: ")

result = llm.stream(user_input)
for chunk in result:
    print(chunk.content, end="")    