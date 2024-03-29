# -*- coding: utf-8 -*-
! pip install langchain-openai
! pip install langchain
! pip install langchain-community
! pip install arxiv
! pip install torch
! %pip install --upgrade --quiet  arxiv
! %pip install --upgrade --quiet  pymupdf
! pip install anyscale
! pip install pymupdf

from langchain import hub
from langchain.agents import AgentExecutor, create_react_agent, load_tools
from langchain_community.chat_models import ChatOpenAI
import os
from getpass import getpass
from langchain.agents import AgentExecutor, AgentType, load_tools, initialize_agent
from langchain.chat_models import ChatAnyscale
from langchain_openai import OpenAIEmbeddings

#Arxiv Loader
from langchain_community.document_loaders import ArxivLoader

docs = ArxivLoader(query="1605.08386", load_max_docs=2).load()
len(docs)

docs[0].metadata  # meta-information of the Document

docs[0].page_content[:400]  # all pages of the Document content

#Anyscale Initialization
!pip install langchainhub

import os
from getpass import getpass
from langchain import hub
from langchain.agents import AgentExecutor, create_react_agent, load_tools
from langchain.chat_models import ChatAnyscale
from langchain_openai import OpenAIEmbeddings


from google.colab import userdata

llm = ChatAnyscale(anyscale_api_base="https://api.endpoints.anyscale.com/v1",
                   anyscale_api_key=userdata.get("ANYSCALE_API_KEY"),
                   model_name="mistralai/Mixtral-8x7B-Instruct-v0.1",
                   temperature=0.7,
                   verbose=True)

tools = load_tools(['arxiv'], llm=llm)
#tools = ['arxiv']

agent = initialize_agent(tools = load_tools(['arxiv'], llm=llm), llm = llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)
print(agent.agent.llm_chain.prompt.template)

agent.invoke("Strongest organism in the world")

from langchain.retrievers import ArxivRetriever
retriever = ArxivRetriever(load_max_docs=2)
docs = retriever.get_relevant_documents(query="1605.08386")
docs[0].metadata  # meta-information of the Document

agent = initialize_agent(tools, llm, AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)
print(agent.agent.llm_chain.prompt.template)

agent_chain = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True,)

agent.invoke("Newton's Laws")

agent_chain.invoke("Can you explain the concept of quantum entanglement?")

agent.invoke("Can you explain the concept of quantum entanglement?")

agent.invoke("Tell me, what is the strongest physical force in the universe?")

agent.invoke("Are you able to retrieve data from the arxiv tool?")

"""
    https://colab.research.google.com/github/aicrashcoursewinter24/ailab1BrianMann/blob/final-project-final-draft/textbookAssistant.ipynb
"""
