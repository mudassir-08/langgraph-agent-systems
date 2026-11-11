from typing import TypedDict, List, Union
from langgraph.graph import StateGraph , START, END
from langchain_core.messages import HumanMessage , AIMessage
from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

class AgentState(TypedDict):
  messages: List[Union[HumanMessage, AIMessage]]


llm = ChatGroq(model="openai/gpt-oss-20b")

def process_node(state: AgentState) -> AgentState:
  """ Simple function to generate the answer """

  response = llm.invoke(state["messages"])
  state["messages"].append(AIMessage(content=response.content))
  print(response.content)

  return state

graph = StateGraph(AgentState)
graph.add_node("process",process_node)
graph.add_edge(START, "process")
graph.add_edge("process", END)
agent = graph.compile()

conversation_history = []

user_input = input("Enter:")
while user_input != "exit":
  conversation_history.append(HumanMessage(content=user_input))
  result = agent.invoke({"messages": conversation_history})
  conversation_history= result["messages"]
  user_input= input("Enter: ")

with open("logging.txt", "w") as file:
  file.write("Your Conversation:\n")
  for messages in conversation_history:
    if isinstance(messages, HumanMessage):
      file.write(f"You: {messages.content}\n")
    elif isinstance(messages, AIMessage):
      file.write(f"AI: {messages.content}\n")
  file.write("End of Conversation.")

print("conversation saved to the logging.txt file.")