
from typing import TypedDict, List
from langgraph.graph import StateGraph , START, END
from langchain_core.messages import HumanMessage
from langchain_groq import ChatGroq 
from dotenv import load_dotenv

load_dotenv()

class AgentState(TypedDict):
  message: List[HumanMessage]

llm = ChatGroq(model="openai/gpt-oss-20b")

def process(state: AgentState) -> AgentState:
  response = llm.invoke(state["message"])
  print("AI reponse: ", response.content)
  print(state["message"])
  return state

graph = StateGraph(AgentState)
graph.add_node("processor", process)
graph.add_edge(START, "processor")
graph.add_edge("processor", END)

agent = graph.compile()

user_input = input("Enter: ")
while user_input != "exit":
  agent.invoke({"message": [HumanMessage(content=user_input)]})
  user_input=input("Enter: ")



