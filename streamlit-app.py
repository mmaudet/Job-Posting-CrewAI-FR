from dotenv import load_dotenv

from crewai import Crew

from tasks import Tasks
from agents import Agents

import streamlit as st

load_dotenv()

st.set_page_config(page_icon="👫", layout="wide")


def icon(emoji: str):
    """Shows an emoji as a Notion-style page icon."""
    st.write(
        f'<span style="font-size: 78px; line-height: 1">{emoji}</span>',
        unsafe_allow_html=True,
    )


class HRCrew:
    def __init__(self, company_description, company_domain, hiring_needs, specific_benefits):
        self.company_description = company_description
        self.company_domain = company_domain
        self.hiring_needs = hiring_needs
        self.specific_benefits = specific_benefits
        self.output_placeholder = st.empty()

    def run(self):
        agents = Agents()
        tasks = Tasks()

        # Create Agents
        researcher_agent = agents.research_agent()
        writer_agent = agents.writer_agent()
        review_agent = agents.review_agent()
        
        # Define Tasks for each agent
        research_company_culture_task = tasks.research_company_culture_task(researcher_agent, self.company_description, self.company_domain)
        industry_analysis_task = tasks.industry_analysis_task(researcher_agent, self.company_domain, self.company_description)
        research_role_requirements_task = tasks.research_role_requirements_task(researcher_agent, self.hiring_needs)
        draft_job_posting_task = tasks.draft_job_posting_task(writer_agent, self.company_description, self.hiring_needs, self.specific_benefits)
        review_and_edit_job_posting_task = tasks.review_and_edit_job_posting_task(review_agent, self.hiring_needs)

        # Instantiate the crew with a sequential process
        crew = Crew(
            agents=[researcher_agent, writer_agent, review_agent],
            tasks=[
                research_company_culture_task,
                industry_analysis_task,
                research_role_requirements_task,
                draft_job_posting_task,
                review_and_edit_job_posting_task
            ],
            verbose=True
        )

        result = crew.kickoff()
        self.output_placeholder.markdown(result)

        return result

if __name__ == "__main__":
    icon("✍ Job Posting CrewAI Demo")

    st.subheader("Activez votre équipe d'agents AI pour publier votre prochaine description de poste !",
                 divider="blue", anchor=False)

    with st.sidebar:
        st.image('./images/LINAGORA-logo.png', use_column_width="auto", caption='Made with love and openness')
        st.header("👇 Entrez les détails de votre recherche de talent")
        with st.form("my_form"):

            company_description = st.text_input("Quelle est la description de l'entreprise ?", placeholder="Description détaillée")
            company_domain = st.text_input("Quel est le site web de l'entreprise ?", placeholder="https://www.linagora.com/")
            hiring_needs = st.text_input("Quel type de poste et quelles compétences recherche-vous ?", placeholder="Soyez précis")
            specific_benefits = st.text_input("Quels sont les avantages spécifiques que vous offrez ?", placeholder="Soyez créatif pour attirer les meilleurs talents")
    
            submitted = st.form_submit_button("C'est parti !")
            
        st.divider()

        # Credits to joaomdmoura/CrewAI for the code: https://github.com/joaomdmoura/crewAI
        st.sidebar.markdown(
            """
        <center>Built on top of <a href="https://github.com/joaomdmoura/crewAI/ " target="_blank">CrewAI</a> and <a href="https://streamlit.io/ " target="_blank">Streamlit</a>
        </center>""",
            unsafe_allow_html=True
        )


if submitted:
    with st.status("🤖 **Processus de génération en cours...**", state="running", expanded=True) as status:
        with st.container(height=500, border=False):
        #with st.container():
            HR_crew = HRCrew(company_description, company_domain, hiring_needs, specific_benefits)
            result = HR_crew.run()
        status.update(label="✅ Fiche de poste disponible !",
                      state="complete", expanded=False)

    st.subheader('Voici votre description de poste complète et définitive. Disponible aussi dans le fichier "offre-emploi.md"', anchor=False, divider="blue")
    st.markdown(result)