from typing import List

from typing_extensions import TypedDict
from lang_node import generateflowchart, Code_Selector
from langgraph.graph import END, StateGraph, START

class GraphState(TypedDict):
    """
    Represents the state of our graph.

    Attributes:
        question: question
        generation: LLM generation

    """

    question: str
    generation: str
    Context_js: str

workflow = StateGraph(GraphState)
workflow.add_node("flowchart", generateflowchart)
workflow.add_node("filter", Code_Selector)
workflow.add_edge(START, "flowchart")
workflow.add_edge("flowchart", "filter")
workflow.add_edge("filter", END)
app1 = workflow.compile()
