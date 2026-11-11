from typing import TypedDict , Annotated, Sequence
from dotenv import load_dotenv

from langchain_core.messages import HumanMessage, AIMessage, BaseMessage, SystemMessage 
from langchain_core.tools import tool 
from langchain_groq import ChatGroq
from langchain_core.messages import ToolMessage

from langgraph.graph import StateGraph, START, END
from langgraph.prebuilt import ToolNode
from langgraph.graph.message import add_messages 


load_dotenv()
class AgentState(TypedDict):
  messages : Annotated[Sequence[BaseMessage], add_messages]

document_content = ""

@tool
def update(content:str)->str:
  """Simple tool which can update the content of the document"""
  global document_content
  document_content= content
  return f"Content of the document is updated successfully! : {document_content}"

@tool
def save(filename:str)->str:
  """Simple function that can used to save the uodated content to the file.
  Args: 
      filename: Name of the text file.
  """
  global document_content

  if not filename.endswith(".txt"):
    filename= f"{filename}.txt"

  try:
    with open(filename, 'w', encoding='utf-8') as file:
      file.write(document_content)
      print(f"Document is saved to the {filename} file successfully!")
      return f"Document is successfully saved to the {filename} file."
  except Exception as e:
    print(f"Error in saving file :{str(e)}")

tools = [update, save]
model = ChatGroq(model="openai/gpt-oss-20b").bind_tools(tools)
system_message = SystemMessage(content =f"""
You are a Drafter. A helpful writing assistant. you are going to help user by updating and savin his documents.
if user wants to update then use the update tool.
if user wants to save to updated document then use the save tool.
make sure to show the current document content after the modifications.

the currrent document content is:{document_content}
""")

def our_agent(state:AgentState)->AgentState:

  if not state["messages"]:
    user_input = "I am ready to help you. What would you like to create?"
    user_message = HumanMessage(content = user_input)
  else:
    user_input = input("\nWhat would you like to do with the document?")
    print(f"\nUser: {user_input}\n")
    user_message = HumanMessage(content=user_input)

  all_messages = [system_message] + list(state["messages"]) + [user_message]

  response = model.invoke(all_messages)

  print(f"\n AI:{response.content}")
  if hasattr(response, "tool_calls") and response.tool_calls:
    print(f"using tools: {[tc['name'] for tc in response.tool_calls]}")

  return {"messages": list(state["messages"])+ [user_message, response]}

def should_continue(state: AgentState)-> str:
  """Simple conditional edge function that decides where to go next"""
  messages = state["messages"]
  if not messages:
    return "continue"

  for message in reversed(messages):
    if (isinstance(message, ToolMessage) and
        "saved" in message.content.lower() and
        "document" in message.content.lower()):
      return "end"
  return "continue"

def print_messages(messages):
  """Funtion that is used to print the messages."""
  if not messages:
    return
  for message in messages[-3:]:
    if isinstance(message, ToolMessage):
      print(f" Tool Result:{message.content}") 

graph = StateGraph(AgentState)
graph.add_node("agent", our_agent)
graph.add_node("tools", ToolNode(tools))
graph.set_entry_point("agent")
graph.add_edge("agent", "tools")

graph.add_conditional_edges(
  "tools",
  should_continue,
  {
    "continue":"agent",
    "end": END
  }
)
    
app = graph.compile()


def run_document_agent():
  print("====== DRAFTER =======")
  state = {"messages":[]}

  for step in app.stream(state,stream_mode="values"):
    if "messages" in step:
      print_messages(step["messages"])

  print("===== DRAFTER FINISHED =====")

if __name__ == "__main__":
  run_document_agent()
