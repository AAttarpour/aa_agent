"""
- This code has written by Ahmadreza Attarpour (a.attarpour@mail.utoronto.ca)
- It creates a chatbot using Langgraph
"""

from langgraph.graph import StateGraph, MessagesState, START, END
from typing import Annotated, Literal, TypedDict
from langchain_core.tools import tool
from langchain_core.messages import HumanMessage
from langgraph.checkpoint.memory import MemorySaver
from langgraph.prebuilt import ToolNode
from langchain_groq import ChatGroq
from langchain_tavily import TavilySearch
from dotenv import load_dotenv
import os

load_dotenv()

# Read the variable from the environment and set it as a env variable
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
LANGCHAIN_API_KEY = os.getenv("LANGCHAIN_API_KEY")
LANGCHAIN_PROJECT = os.getenv("LANGCHAIN_PROJECT")
if GOOGLE_API_KEY:
    os.environ["GOOGLE_API_KEY"] = GOOGLE_API_KEY
if LANGCHAIN_API_KEY:
    os.environ["LANGCHAIN_API_KEY"] = LANGCHAIN_API_KEY
if LANGCHAIN_PROJECT:
    os.environ["LANGCHAIN_PROJECT"] = LANGCHAIN_PROJECT
if os.getenv("GROQ_API_KEY"):
    os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")
if os.getenv("SERPER_API_KEY"):
    os.environ["SERPER_API_KEY"] = os.getenv("SERPER_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_ENDPOINT"] = "https://api.smith.langchain.com"

class Chatbot:

    def __init__(self):
        self.llm = ChatGroq(model_name="Gemma2-9b-It")

    def call_tool(self):
        tool = TavilySearch(max_results=3)
        tools = [tool]
        self.tool_node = ToolNode(tools=tools)
        self.llm_with_tool = self.llm.bind_tools(tools)

    def call_model(self, state: MessagesState):
        messages = state["messages"]
        response = self.llm_with_tool.invoke(messages)
        return {"messages": [response]}
    
    def router_function(self, state: MessagesState) -> Literal["tools", END]:
        """
        This function routes the state to the tools if the query is related to 'reza'.
        """
        messages = state['messages']
        last_message = messages[-1] 

        if last_message.tool_calls:
            return "tools"

        return END
    
    def __call__(self):
        self.call_tool()
        workflow = StateGraph(MessagesState)
        workflow.add_node("agent", self.call_model)
        workflow.add_node("tools", self.tool_node)
        workflow.add_edge(START, "agent")
        workflow.add_conditional_edges(
            "agent", # starts from here 
            self.router_function, # this decides the next step
            {"tools": "tools", END: END} # either go to tools or end
        )  
        workflow.add_edge("tools", "agent")
        self.app = workflow.compile()
        return self.app


if __name__ == "__main__":
    mybot = Chatbot() # run the __init__ method
    workflow = mybot() # run the __call__ method
    response = workflow.invoke({"messages": [HumanMessage(content="Who is the current prime minister of Canada?")]})
    print(response['messages'][-1].content) 