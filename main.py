from dotenv import load_dotenv
from pydantic import BaseModel
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from langchain.agents import create_tool_calling_agent, AgentExecutor
from tools import search_tool, wiki_tool, save_tool
import os
import google.generativeai as genai

load_dotenv()

class ResearchResponse(BaseModel):
    topic: str
    summary: str
    sources: list[str]
    tools_used: list[str]
    
gemini_api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key = "AIzaSyDe8_ru7Y-503iBt8HMqf4yyGKRyoTOubA")
llm = genai.GenerativeModel("gemini-2.5-pro")


def gemini_agent(user_input):
    response = llm.generate_content(user_input)
    return response.text
if __name__ == "__main__":
    print("Hello! welcome to FirstDateAI we are here to help you on your first date")
    print("Would you like help with fashion first? (y/n)")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Goodbye!")
            break
        elif user_input.lower() in ["y"]:
            print("We got you")
        reply = gemini_agent(user_input)
        print("Gemini:", reply)
