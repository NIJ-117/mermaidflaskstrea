# Define tasks
from crewai import Agent, Task, Crew, Process
from agent import network_architect, security_specialist, devops_engineer,documentation_specialist

design_network = Task(
    description=(
        "Design the {architecture_type} network architecture following the best practices."
        "Ensure the design includes scalability, redundancy, and efficient use of resources."
    ),
    expected_output='A structured network architecture asked in bullet points with the technical details',
    agent=network_architect,
)

perform_security_assessment = Task(
    description=(
        "Provide recommendations for improving the security of the {architecture_type}"
    ),
    expected_output=' Add the security features on the architecture to enhance the security',
    agent=security_specialist,
)
ci_cd = Task(
    description='Set up CI/CD pipelines and automate deployment processes for the given architecture ',
    agent=devops_engineer,
    expected_output='add the CI/CD pipeline configurations, scripts, and automation workflows to the architecture'
)

create_documentation = Task(
    description='Create detailed documentation and diagrams for the network architecture, incorporating outputs from architecture design, security implementation, and CI/CD setup',
    agent=documentation_specialist,
    expected_output='Provide detailed documentation on the user query in pointer system with all the necessary details to implement the architecture following the information given by the user'
)