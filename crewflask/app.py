from flask import Flask, render_template, request, jsonify, send_file
import concurrent.futures
from pprint import pprint
from io import BytesIO

from creew import crew1, crew2, crew3, crew4  # Ensure these modules are correctly imported
from lang_graph import app1



app = Flask(__name__)

# Function to kickoff a crew
def kickoff_crew(crew, inputs):
    return crew.kickoff(inputs=inputs)

def generate_documentation(question):
    architecture_type = question
    inputs = {'architecture_type': architecture_type}

    with concurrent.futures.ThreadPoolExecutor() as executor:
        future1 = executor.submit(kickoff_crew, crew1, inputs)
        future2 = executor.submit(kickoff_crew, crew2, inputs)
        future3 = executor.submit(kickoff_crew, crew3, inputs)

        result1 = future1.result()
        result2 = future2.result()
        result3 = future3.result()
        # result2=""
        # result3=""

    text = f"The Network architecture for the {architecture_type} is {result1} and the security assessment is {result2} and the CI/CD pipelines are {result3}"
    
    inputs = {
        'architecture_type': architecture_type,
        'text': text
    }

    result = crew4.kickoff(inputs=inputs)
    context = str(result)  # Convert to string if necessary

    return context

def generate_mermaid_code(question, context):
    inputs = {
        "question": question,
        "Context_js": context
    }

    final_result = None
    for output in app1.stream(inputs):
        for key, value in output.items():
            pprint(f"Node '{key}':")
        final_result = str(value["generation"])  # Convert to string if necessary

    return final_result

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_documentation', methods=['POST'])
def generate_documentation_route():
    question = request.form['question']
    documentation_text = generate_documentation(question)
    return jsonify({'documentation_text': documentation_text})

@app.route('/generate_code', methods=['POST'])
def generate_code_route():
    question = request.form['question']
    context = request.form['context']
    mermaid_code = generate_mermaid_code(question, context)
    return jsonify({'mermaid_code': mermaid_code})

@app.route('/download_code', methods=['POST'])
def download_code():
    code = request.form['code']
    buffer = BytesIO()
    buffer.write(code.encode('utf-8'))
    buffer.seek(0)
    return send_file(buffer, as_attachment=True, download_name='mermaid_code.txt', mimetype='text/plain')

@app.route('/download_documentation', methods=['POST'])
def download_documentation():
    documentation = request.form['documentation']
    buffer = BytesIO()
    buffer.write(documentation.encode('utf-8'))
    buffer.seek(0)
    return send_file(buffer, as_attachment=True, download_name='documentation.txt', mimetype='text/plain')

@app.route('/update_diagram', methods=['POST'])
def update_diagram():
    node_data = request.form['nodeData']
    current_markdown = request.form['currentMarkdown']
    updated_markdown = current_markdown + "\n" + node_data  # Example update logic
    return jsonify({'updatedMarkdown': updated_markdown})

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=4001)
