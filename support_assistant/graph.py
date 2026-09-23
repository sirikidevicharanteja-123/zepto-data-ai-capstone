#import required libraries

import os
from typing import TypedDict

from langgraph.graph import StateGraph, START, END

from retrieval import retrieve_documents

# LLM mode configuration
MOCK_LLM = os.getenv("MOCK_LLM", "1") == "1"

# Graph state
class GraphState(TypedDict):
    query: str
    intent: str
    answer: str
    sources: list
    confidence: float

# Classify user intent

def classify_intent(state: GraphState):
    query = state["query"].lower()

    policy_keywords = [
        "delivery",
        "return",
        "refund",
        "membership",
        "tracking",
        "cancel",
        "gift card",
        "support hours"
    ]

    if MOCK_LLM:
        if any(keyword in query for keyword in policy_keywords):
            intent = "policy_question"
        else:
            intent = "general_question"

    return {
        "intent": intent
    }

# Retrieve relevant documents and generate answer

def retrieve_and_answer(state: GraphState):
    query = state["query"]

    retrieved_documents, retrieved_ids = retrieve_documents(query)

    top_chunk = retrieved_documents[0]

    if MOCK_LLM:
        answer = f"Based on the retrieved context: {top_chunk[:200]}"
        confidence = 1.0

    return {
        "answer": answer,
        "sources": retrieved_ids,
        "confidence": confidence
    }
# Handle general questions

def direct_answer(state: GraphState):
    if MOCK_LLM:
        return {
            "answer": "I can only answer questions about Zepto policies right now.",
            "sources": [],
            "confidence": 1.0
        }
# Route based on intent

def route_intent(state: GraphState):
    if state["intent"] == "policy_question":
        return "retrieve_and_answer"

    return "direct_answer"
  

# Build LangGraph

builder = StateGraph(GraphState)

builder.add_node("classify_intent", classify_intent)
builder.add_node("retrieve_and_answer", retrieve_and_answer)
builder.add_node("direct_answer", direct_answer)

builder.add_edge(START, "classify_intent")

builder.add_conditional_edges(
    "classify_intent",
    route_intent,
    {
        "retrieve_and_answer": "retrieve_and_answer",
        "direct_answer": "direct_answer"
    }
)

builder.add_edge("retrieve_and_answer", END)
builder.add_edge("direct_answer", END)

graph = builder.compile()
