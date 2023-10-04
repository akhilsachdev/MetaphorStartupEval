import streamlit as st
from metaphor_agent import agent_executor

#UI for an LLM agent that evaluates startups

st.title("Metaphor Startup Evaluator")
st.markdown("This application is designed to help you evaluate your startup's potential for success using Metaphor and Langchain agents.")
st.markdown("Please enter the information below to get started!")
st.markdown("")

#Startup Name
st.header("Startup Name")
st.markdown("Please enter the name of your startup below.")
startup_name = st.text_input("Startup Name")
agent_output = None

#use agent executor to run the agent on startup name add button to run agent
if st.button("Evaluate Startup"):
    #run agent on startup name
    #Show loading bar

    #display output in a list
    st.header("Startup Evaluation")
    st.markdown("The evaluation of your startup is displayed below.")
    st.markdown("")
    with st.spinner("Evaluating Startup..."):
        agent_output = agent_executor.invoke({"input": "Evaluate the potential of " + startup_name})
    #Loading if agent is running
    
    st.write(agent_output['output'])



# agent_output = agent_executor.invoke({"input": "Evalute the potential of " + startup_name})





