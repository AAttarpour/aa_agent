"""
- This code has written by Ahmadreza Attarpour (a.attarpour@mail.utoronto.ca)
- It uses streamlit to create a chatbot interface
"""


import streamlit as st
from transformers import pipeline
from aa_bot import Chatbot
from langchain_core.messages import HumanMessage


mybot = Chatbot()
workflow = mybot()


# set up the streamlit app UI
st.title("Reza's Chatbot with Langgraph")
st.write("Ask any question, and I'll try to answer :)")


# Input text box for the question
question = st.text_input("Ask your question here:")
input = {"messages": [HumanMessage(content=question)]}



# button to get the response
if st.button("Get Answer"):
    if input:

        response = workflow.invoke(input)
        st.write("**Answer:**", response['messages'][-1].content)
        
    else:

        st.warning("Please enter a question.")


# Additional styling
st.markdown("---")
st.caption("This is a simple chatbot interface powered by Streamlit and Transformers.")