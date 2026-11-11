from typing import Annotated, Sequence , TypedDict
from langchain_core.messages import BaseMessage
from langchain_core.messages import SystemMessage
from langchain_core.messages import ToolMessage
from langchain_groq import ChatGroq
from langchain_core.tools import tool
from dotenv import load_dotenv
from langgraph.graph.message import add_messages
from langgraph.graph import StateGraph, START , END
from langgraph.prebuilt import ToolNode

load_dotenv()

class AgentState(TypedDict):
  messages : Annotated[Sequence[BaseMessage], add_messages]

@tool
def add( a:int, b:int ):
  """Simple function which add 2 numbers together"""
  return a+b

@tool 
def subtract(a:int , b:int ):
  """Simple function which is used to subtract to numbers"""
  return a-b

@tool
def multiply(a:int,b: int):
  """Simple function that is used to multiply 2 numbers"""
  return a*b

tools = [add, subtract, multiply]
model = ChatGroq(model="openai/gpt-oss-20b").bind_tools(tools)
system_prompt = SystemMessage(content="Your are a helpful assistant. Your name is Gogpt.")

def model_call(state: AgentState) -> AgentState:
  response = model.invoke([system_prompt] + state["messages"])
  return {"messages":[response]}

def continue_edge(state: AgentState) -> AgentState:
  messages = state["messages"]
  last_message = messages[-1]

  if not last_message.tool_calls:
    return "exit"
  else:
    return "continue"


graph = StateGraph(AgentState)
graph.add_node("agent_node", model_call)

tool_node1= ToolNode(tools=tools)
graph.add_node("tool_node", tool_node1)
graph.add_conditional_edges(
  "agent_node",
  continue_edge,
  {
    "exit":END,
    "continue": "tool_node"
  }
)
graph.set_entry_point("agent_node")
graph.add_edge("tool_node","agent_node")

agent = graph.compile()

def print_stream(stream):
  for s in stream:
    message = s["messages"][-1]
    if isinstance(message, tuple):
      print(message)
    else:
      message.pretty_print()

inputs = {"messages": [("User : add 3+4 then multiply it's result by 2")]}
print_stream(agent.stream(inputs, stream_mode="values"))
