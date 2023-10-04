# Metaphor Startup Evaluation

## Description
This application uses an LLM agent that works with Metaphor to evaluate a startup based on their business model, competitors, target market, and growth potential. The technologies I used were Langchain, Python, Streamlit, OpenAI, and Metaphor API.

## Potential Improvements
The intent of the application is to ultimately do due dilligence to evaluate startups from an investing perspective. In the future additional tools to get and create numerical data about the company and it's potential for growth would need to be added to the agent. LLM-context length is an issue as well, but this can be solved through vector databases and prompt compression.

## How to run
1. Create a conda environment with Python 3.10 `conda create -n metaphor python=3.10`
2. Install the requirements by running `pip install -m requirements.txt`
3. Use this command to start the application `streamlit run streamlit_main.py`