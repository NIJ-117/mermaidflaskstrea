from crewai import Agent, Task, Crew, Process
from agent import network_architect, security_specialist, devops_engineer, documentation_specialist
from task import design_network, perform_security_assessment, ci_cd, create_documentation
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

crew4 = Crew(
        agents=[documentation_specialist],
        tasks=[create_documentation],
        process=Process.sequential
    )
