from typing import Dict, TypedDict
from langgraph.graph import StateGraph

class AgentState(TypedDict):
  message : str

def greeting_node(state: AgentState) -> StateGraph:
  state["message"] = "Hey "+ state["message"] + ", How are you?"
  return state

graph = StateGraph(AgentState)
graph.add_node("Greeter", greeting_node)
graph.set_entry_point("Greeter")
graph.set_finish_point("Greeter")

app = graph.compile()

from IPython.display import Image, display
display(Image(app.get_graph().draw_mermaid_png()))