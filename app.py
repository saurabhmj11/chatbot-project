# app.py

import streamlit as st
from langchain_community.utilities import ArxivAPIWrapper, WikipediaAPIWrapper
from langchain_community.tools import ArxivQueryRun, WikipediaQueryRun
from langgraph.graph.message import add_messages
from langgraph.graph import StateGraph, START, END
from langchain_groq import ChatGroq
from google.colab import userdata

# Arxiv and Wikipedia setup
arxiv_wrapper = ArxivAPIWrapper(top_k_results=1, doc_content_chars_max=300)
arxiv_tool = ArxivQueryRun(api_wrapper=arxiv_wrapper)

wiki_wrapper = WikipediaAPIWrapper(top_k_results=1, doc_content_chars_max=300)
wiki_tool = WikipediaQueryRun(api_wrapper=wiki_wrapper)

tools = [wiki_tool, arxiv_tool]

# Setup Langgraph application and chatbot function
class State(TypedDict):
    messages: Annotated[list, add_messages]

graph_builder = StateGraph(State)

# Initialize Groq LLM
groq_api_key = userdata.get("groq_api_key")
llm = ChatGroq(groq_api_key=groq_api_key, model_name="Gemma2-9b-It")
llm_with_tools = llm.bind_tools(tools=tools)

def chatbot(state: State):
    return {"messages": [llm_with_tools.invoke(state["messages"])]}

# Add chatbot and tool nodes to the graph
graph_builder.add_node("chatbot", chatbot)
tool_node = ToolNode(tools=tools)
graph_builder.add_node("tools", tool_node)

graph_builder.add_conditional_edges("chatbot", tools_condition)
graph_builder.add_edge("tools", "chatbot")
graph_builder.add_edge(START, "chatbot")

graph = graph_builder.compile()

# --- Streamlit Web Interface ---
st.title("AI-Powered Chatbot with Arxiv and Wikipedia")

# Text input box for user input
user_input = st.text_input("Enter your query here:", "")

# Submit button
if st.button("Submit"):
    if user_input:
        # Process the user input through the chatbot graph
        events = graph.stream({"messages": [("user", user_input)]}, stream_mode="values")
        
        # Display the chatbot response
        for event in events:
            response = event["messages"][-1]
            st.write(f"**Bot:** {response.content}")

# Additional Instructions for Display
st.write("This chatbot uses Arxiv and Wikipedia APIs to fetch real-time information and provide insightful responses. You can ask anything related to research or general knowledge!")

