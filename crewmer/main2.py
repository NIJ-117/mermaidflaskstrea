import os
from crewai import Agent, Task, Crew, Process
import streamlit as st
from lang_graph import GraphState
from lang_node import generateflowchart, Code_Selector
from langgraph.graph import END, StateGraph, START
import gradio as gr
from pprint import pprint
import os
from crewai import Crew, Process
from agent import network_architect, security_specialist, devops_engineer, documentation_specialist
from task import design_network, perform_security_assessment, ci_cd, create_documentation
import concurrent.futures
import streamlit.components.v1 as components
import tempfile

def process_question(question):
    # Define the first crew
    crew1 = Crew(
        agents=[network_architect],
        tasks=[design_network],
        process=Process.sequential
    )

    crew2 = Crew(
        agents=[security_specialist],
        tasks=[perform_security_assessment],
        process=Process.sequential
    )

    crew3 = Crew(
        agents=[devops_engineer],
        tasks=[ci_cd],
        process=Process.sequential
    )

    # Function to kickoff a crew
    def kickoff_crew(crew, inputs):
        return crew.kickoff(inputs=inputs)


    architecture_type = question
    # Inputs for the crews
    inputs = {
        'architecture_type': architecture_type
    }

    # Using ThreadPoolExecutor to run crews in parallel
    with concurrent.futures.ThreadPoolExecutor() as executor:
        future1 = executor.submit(kickoff_crew, crew1, inputs)
        future2 = executor.submit(kickoff_crew, crew2, inputs)
        future3 = executor.submit(kickoff_crew, crew3, inputs)

        result1 = future1.result()
        result2 = future2.result()
        result3 = future3.result()

    print(result1)
    print(result2)
    print(result3)

    text=f"The Network architecture for the {architecture_type} is {result1} and the security assessment is {result2} and the CI/CD pipelines are {result3}"

    Crew4 = Crew(
        agents=[documentation_specialist],
        tasks=[create_documentation],
        process=Process.sequential
    )
    inputs = {
        'architecture_type': architecture_type,
        'text': text
    }

    result=Crew4.kickoff(inputs=inputs)
    print(result)

    workflow = StateGraph(GraphState)
    workflow.add_node("flowchart", generateflowchart)
    workflow.add_node("filter", Code_Selector)
    workflow.add_edge(START,"flowchart")
    workflow.add_edge("flowchart", "filter")
    workflow.add_edge("filter", END)
    app = workflow.compile()

    
    context = result
    result_code = ""

    inputs = {
        "question": f"{question}",
        "Context_js": f"{context}"
    }

    for output in app.stream(inputs):
        for key, value in output.items():
            pprint(f"Node '{key}':")
        pprint("\n---\n")

    final_result = value["generation"]
    return final_result

# Function to render Mermaid code
def mermaid(code: str) -> None:
    components.html(
        f"""
        <pre class="mermaid">
            {code}
        </pre>
        <script type="module">
            import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.esm.min.mjs';
            mermaid.initialize({{ startOnLoad: true }});
        </script>
        """,
        height=2000,  # Adjust height as needed
    )


# Streamlit app
st.title("Mermaid js conversion with the LLM ")
st.write("Enter a question")

question = st.text_input("Question")



if st.button("Generate"):
    if question:
        result = process_question(question)
         # Strip the surrounding triple backticks
        st.write("Generated Mermaid.js code:")
        st.text_area("Mermaid.js Code", result, height=200)

        # Save the Mermaid.js code to a temporary file
        temp_file_path = os.path.join(tempfile.gettempdir(), "mermaid_code.txt")
        with open(temp_file_path, "w") as file:
            file.write(result)
        st.session_state["mermaid_code_file"] = temp_file_path
        st.session_state["mermaid_code"] = result
    else:
        st.error("Please enter a question.")

# Button to display the Mermaid diagram
if "mermaid_code_file" in st.session_state and st.button("Display Mermaid Diagram"):
    with open(st.session_state["mermaid_code_file"], "r") as file:
        mermaid_code = file.read()
        st.write("Diagram:")
        mermaid(mermaid_code)


