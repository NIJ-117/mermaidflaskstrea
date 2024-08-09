from langchain_community.tools import DuckDuckGoSearchRun


search_tool = DuckDuckGoSearchRun()
query = "current weather in New York"
resutl=search_tool(query)
print(resutl)