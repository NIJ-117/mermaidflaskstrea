import os
import streamlit as st
import streamlit.components.v1 as components
import concurrent.futures
from pprint import pprint

from lang_graph import app1

from creew import crew1, crew2, crew3, crew4

# Function to kickoff a crew
def kickoff_crew(crew, inputs):
    return crew.kickoff(inputs=inputs)

def generate_documentation(question):
    # Define the first crew
    architecture_type = question
    inputs = {'architecture_type': architecture_type}

    # Using ThreadPoolExecutor to run crews in parallel
    with concurrent.futures.ThreadPoolExecutor() as executor:
        future1 = executor.submit(kickoff_crew, crew1, inputs)
        future2 = executor.submit(kickoff_crew, crew2, inputs)
        future3 = executor.submit(kickoff_crew, crew3, inputs)

        result1 = future1.result()
        result2 = future2.result()
        result3 = future3.result()

    text = f"The Network architecture for the {architecture_type} is {result1} and the security assessment is {result2} and the CI/CD pipelines are {result3}"
    
    inputs = {
        'architecture_type': architecture_type,
        'text': text
    }

    result = crew4.kickoff(inputs=inputs)

    context = result
    return str(context)  # Convert context to string if necessary

def generate_mermaid_code(question, context):
    inputs = {
        "question": question,
        "Context_js": context
    }

    final_result = None
    for output in app1.stream(inputs):
        for key, value in output.items():
            pprint(f"Node '{key}':")
        final_result = value["generation"]

    return str(final_result)  # Convert final_result to string if necessary

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
        height=3000,  # Adjust height as needed
    )

# Streamlit app

st.title("Mermaid.js Conversion with the LLM")
with st.sidebar:
    
    st.write("Enter a question")

    question = st.text_input("Question")

    # Generate Documentation Button
    if st.button("Generate Documentation"):
        if question:
            documentation_text = generate_documentation(question)
            # Store documentation in session state
            st.session_state["documentation_text"] = documentation_text
        else:
            st.error("Please enter a question.")

    # Generate Mermaid Code Button
    if st.button("Generate Mermaid Code"):
        if "documentation_text" in st.session_state:
            mermaid_code = generate_mermaid_code(question, st.session_state["documentation_text"])
            st.session_state["mermaid_code"] = mermaid_code
        else:
            st.error("Please generate documentation first.")

# Display the generated Mermaid.js code in an editable text area
if "mermaid_code" in st.session_state:
    with st.sidebar:
        st.write("Generated Mermaid.js code:")
        mermaid_code = st.text_area("Mermaid.js Code", st.session_state["mermaid_code"], height=200, key="mermaid_code_area")

        if st.button("Display Mermaid Diagram"):
            # Update the session state with the current text area content
            st.session_state["mermaid_code"] = mermaid_code
            st.session_state["display_diagram"] = True

        st.download_button(
            label="Download Mermaid.js Code",
            data=mermaid_code,
            file_name="mermaid_code.txt",
            mime="text/plain"
        )

        # Button to download the documentation
        if "documentation_text" in st.session_state:
            st.download_button(
                label="Download Documentation",
                data=st.session_state["documentation_text"],
                file_name="network_documentation.txt",
                mime="text/plain"
            )

if "documentation_text" in st.session_state:
    st.write("### Documentation")
    st.write(st.session_state["documentation_text"])

# Main area to display the Mermaid diagram
if "mermaid_code" in st.session_state and st.session_state.get("display_diagram", False):
    mermaid(st.session_state["mermaid_code"])
