import os
from crewai import Agent, Task, Crew, Process
from llm import llm_model2,llm_model_devops,llm_model_network,llm_model_security
from tools import search_tool

# Define agents
network_architect = Agent(
    role='Network Architect',
    goal='Design a robust and scalable network architecture following best practicesfor the user query {architecture_type} and in the search tool use str as input for the query.',
    verbose=True,
    memory=True,
    backstory="You are a cloud network architect responsible for designing and implementing network infrastructure.",
    tools=[search_tool],
    llm=llm_model_network,
    max_iter=1
)

security_specialist = Agent(
    role='Security Specialist',
    goal='Implement the best security practices for  {architecture_type} and in the search tool use str as input for the query.',
    verbose=True,
    memory=True,
    backstory="Your duty is implement the best security features available for the given network architecture",
    tools=[search_tool],
    llm=llm_model_security,
    
    max_iter=1
)
devops_engineer = Agent(
    role='DevOps Engineer',
    goal='Set up CI/CD pipelines and automate deployment processes for the {architecture_type} and in the search tool use str as input for the query.',
    backstory="A DevOps engineer skilled in automation, CI/CD pipelines, and infrastructure as code (IaC).",
    tools=[search_tool],
    memory=True,
    verbose=True,
    llm=llm_model_devops,
    max_iter=1
)

documentation_specialist = Agent(
    role='Documentation Specialist',
    goal='Create detailed documentation on the basis of the text provided for the query {architecture_type} the text we have is {text}',
    backstory="An expert in technical writing and documentation.",
    memory=True,
    verbose=True,
    llm=llm_model_devops,
    max_iter=2
)
