from dotenv import load_dotenv
load_dotenv()

from crewai import Crew

from tasks import Tasks
from agents import Agents

from textwrap import dedent

tasks = Tasks()
agents = Agents()

company_description = input("Quelle est la description de l'entreprise ?\n")
company_domain = input("Quel est le site web de l'entreprise ?\n")
hiring_needs = input("Quel type de poste et quelles compétences recherche-vous ?\n")
specific_benefits = input("Quels sont les avantages spécifiques que vous offrez ?\n")

# Create Agents
researcher_agent = agents.research_agent()
writer_agent = agents.writer_agent()
review_agent = agents.review_agent()

# Define Tasks for each agent
research_company_culture_task = tasks.research_company_culture_task(researcher_agent, company_description, company_domain)
industry_analysis_task = tasks.industry_analysis_task(researcher_agent, company_domain, company_description)
research_role_requirements_task = tasks.research_role_requirements_task(researcher_agent, hiring_needs)
draft_job_posting_task = tasks.draft_job_posting_task(writer_agent, company_description, hiring_needs, specific_benefits)
review_and_edit_job_posting_task = tasks.review_and_edit_job_posting_task(review_agent, hiring_needs)

# Instantiate the crew with a sequential process
crew = Crew(
    agents=[researcher_agent, writer_agent, review_agent],
    tasks=[
        research_company_culture_task,
        industry_analysis_task,
        research_role_requirements_task,
        draft_job_posting_task,
        review_and_edit_job_posting_task
    ]
)

# Kick off the process
result = crew.kickoff()

print("Processus de création d'offres d'emploi achevé.")
print('Vous pouvez prendre connaissance du fichier "offre-emploi.md"')
print(result)