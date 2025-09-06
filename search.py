from dotenv import load_dotenv
import os
from langchain_core.prompts import PromptTemplate
from langchain_groq import ChatGroq
from langchain_ollama import ChatOllama
#from langchain-tavily import TavilySearch 
#from langchain_tavily import TavilySearch 
#from langchain_community.tools.tavily_search import TavilySearch
#from :class:`~langchain_tavily import TavilySearch
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain import hub
from langchain.agents import AgentExecutor
from langchain.agents.react.agent import create_react_agent

load_dotenv()

tools = [TavilySearchResults()]
#tools = [TavilySearc()]
#llm=ChatOllama(model="llama3")
llm=ChatGroq(model="Gemma2-9b-It",groq_api_key= os.getenv("GROQ_API_KEY") )
react_prompt = hub.pull("hwchase17/react")
agent = create_react_agent(
    llm=llm,
    tools=tools,
    prompt=react_prompt,)
agent_executor = AgentExecutor(
    agent=agent, 
    tools=tools, 
    verbose=True,
    handle_parsing_errors=True)
chain = agent_executor

def main():
    result = chain.invoke(
        input={
            "input": "search for 3 job postings for an ai engineer using langchain in the bay area on linkedin and list their details",
        })
    print(result)

if __name__ == "__main__":
    main()

