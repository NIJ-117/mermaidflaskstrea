import os
from crewai import Agent, Task, Crew, Process
from langchain_community.tools import DuckDuckGoSearchRun

# Define the tools to be used
search_tool = DuckDuckGoSearchRun()