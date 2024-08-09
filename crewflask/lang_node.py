from langchain.schema import Document
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.pydantic_v1 import BaseModel, Field

from doc import flowchart_documentation,mermaid_documentation,Class_documentation,Sequence_Documentation

from typing import Literal
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.prompts import ChatPromptTemplate, FewShotChatMessagePromptTemplate
from langchain_core.pydantic_v1 import BaseModel, Field
from llm import llm_model2


# LLM with function call




def generateflowchart(state):
    """
    Generate answer

    Args:
        state (dict): The current graph state

    Returns:
        state (dict): New key added to state, generation, that contains LLM generation

    """
    system = "You are mermaid network diagram generating machine which strictly follows this documentation "
    print("we are currently in the flowchart")
    human = "{text}"
    chat = llm_model2
    prompt = ChatPromptTemplate.from_messages([("system", system), ("human", human)])


    question=state["question"]
    Context=state["Context_js"]
    chain = prompt | chat
    # result=chain.invoke({"text": f"for following question {question} we have context {Context} for this context make the flowchart diagram code in mermaid js on basis of following rules {flowchart_context} "})
    result=chain.invoke({"text": f"for following question {question} we have  answer as context {Context} now we have to make the network diagram for this answer in mermaid js using this documentation {flowchart_documentation}. try to use top to down in majority of uses and make detailed flowchart with technical details"})
    result_code=result.content
    print(result.content)
    return {"generation": result.content}


    
def Code_Selector(state):
    """
    Generate answer

    Args:
        state (dict): The current graph state

    Returns:
        state (dict): New key added to state, generation, that contains LLM generation

    """
    examples = [
    {"input": """Sure, here's a sample Mermaid JS code for a simple network diagram illustrating a basic web application architecture:

```mermaid
graph TD
    A[Browser] --> B[Web Server]
    B --> C[Application Server]
    C --> D[Database Server]
    B --> E[Cache Server]
    C --> F[Authentication Service]
    F --> G[OAuth Provider]
    D --> H[Backup Server]
```

In this diagram:
- The browser (A) connects to the web server (B).
- The web server (B) communicates with the application server (C).
- The application server (C) accesses the database server (D) and the cache server (E).
- The application server (C) also communicates with the authentication service (F), which in turn connects to an OAuth provider (G).
- The database server (D) is backed up by the backup server (H).

You can customize this code to fit different architectures or add more components as needed.""", "output": """graph TD
    A[Browser] --> B[Web Server]
    B --> C[Application Server]
    C --> D[Database Server]
    B --> E[Cache Server]
    C --> F[Authentication Service]
    F --> G[OAuth Provider]
    D --> H[Backup Server]"""},
    {"input": """Sure, here's a sample Mermaid JS code for a simple network diagram illustrating a basic web application architecture:

```mermaid
graph TD
    A[Browser] --> B[Web Server]
    B --> C[Application Server]
    C --> D[Database Server]
    B --> E[Cache Server]
    C --> F[Authentication Service]
    F --> G[OAuth Provider]
    D --> H[Backup Server]
```

In this diagram:
- The browser (A) connects to the web server (B).
- The web server (B) communicates with the application server (C).
- The application server (C) accesses the database server (D) and the cache server (E).
- The application server (C) also communicates with the authentication service (F), which in turn connects to an OAuth provider (G).
- The database server (D) is backed up by the backup server (H).

You can customize this code to fit different architectures or add more components as needed.""", "output": """graph TD
    A[Browser] --> B[Web Server]
    B --> C[Application Server]
    C --> D[Database Server]
    B --> E[Cache Server]
    C --> F[Authentication Service]
    F --> G[OAuth Provider]
    D --> H[Backup Server]"""},
]
    example_prompt = ChatPromptTemplate.from_messages(
    [
        ("human", "{input}"),
        ("ai", "{output}"),
    ]
    )
    few_shot_prompt = FewShotChatMessagePromptTemplate(
        example_prompt=example_prompt,
        examples=examples,
    )

    final_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You  are a machine who works is to filter the mermaid js  code from the answer "),
        few_shot_prompt,
        ("human", "{text}"),
    ]
    )
    
    chat = llm_model2
    

    question=state["question"]
    chain = final_prompt | chat
    result_code=state['generation']
    # result=chain.invoke({"text": f"for following question {question} we have context {Context} for this context make the flowchart diagram code in mermaid js on basis of following rules {flowchart_context} "})
    result=chain.invoke({"text": f"In the following answer {result_code} only give the mermaid js as the output. in the answer avoid(''') and this lead to syntax error and also avoid mermaid before the graph tb/lr "})
    print(result.content)
    print("--------------------------------")
    return {"generation": result.content}
    
