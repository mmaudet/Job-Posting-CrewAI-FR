from crewai import Agent
import streamlit as st
from langchain_community.llms import OpenAI
import os
import openai

openai.api_key = os.environ["OPENAI_API_KEY"]

from crewai_tools.tools import WebsiteSearchTool, SerperDevTool, FileReadTool

web_search_tool = WebsiteSearchTool()
seper_dev_tool = SerperDevTool()
file_read_tool = FileReadTool(
	file_path='exemple_fiche_poste.md',
	description="Un outil pour lire le fichier d'exemple de fiche de poste."
)

def streamlit_callback(step_output):
    # This function will be called after each step of the agent's execution
    st.markdown("---")
    for step in step_output:
        if isinstance(step, tuple) and len(step) == 2:
            action, observation = step
            if isinstance(action, dict) and "tool" in action and "tool_input" in action and "log" in action:
                st.markdown(f"# Action")
                st.markdown(f"**Tool:** {action['tool']}")
                st.markdown(f"**Tool Input** {action['tool_input']}")
                st.markdown(f"**Log:** {action['log']}")
                st.markdown(f"**Action:** {action['Action']}")
                st.markdown(
                    f"**Action Input:** ```json\n{action['tool_input']}\n```")
            elif isinstance(action, str):
                st.markdown(f"**Action:** {action}")
            else:
                st.markdown(f"**Action:** {str(action)}")

            st.markdown(f"**Observation**")
            if isinstance(observation, str):
                observation_lines = observation.split('\n')
                for line in observation_lines:
                    if line.startswith('Title: '):
                        st.markdown(f"**Title:** {line[7:]}")
                    elif line.startswith('Link: '):
                        st.markdown(f"**Link:** {line[6:]}")
                    elif line.startswith('Snippet: '):
                        st.markdown(f"**Snippet:** {line[9:]}")
                    elif line.startswith('-'):
                        st.markdown(line)
                    else:
                        st.markdown(line)
            else:
                st.markdown(str(observation))
        else:
            st.markdown(step)

class Agents():
	def research_agent(self):
		return Agent(
			role='Expert en recherche',
			goal="Analyser le site web de l'entreprise et la description fournie pour en tirer des informations sur la culture, les valeurs et les besoins spécifiques.",
			tools=[web_search_tool, seper_dev_tool],
			backstory="Tu es un expert dans l'analyse des cultures d'entreprise et l'identification des valeurs et des besoins clés à partir de diverses sources, y compris des sites web et des descriptions succinctes.",
			verbose=True,
            step_callback=streamlit_callback,
		)

	def writer_agent(self):
			return Agent(
				role='Expert en écriture de fiche de poste',
				goal="Utiliser les informations fournies par l'expert en recherche pour créer une offre d'emploi détaillée, attrayante et séduisante.",
				tools=[web_search_tool, seper_dev_tool, file_read_tool],
				backstory="Tu as toutes les compétences en matière de rédaction de descriptions de postes convaincantes qui correspondent aux valeurs de l'entreprise et qui attirent les bons candidats.",
				verbose=True,
        		step_callback=streamlit_callback,
			)

	def review_agent(self):
			return Agent(
				role="Expert en révision de contenus et de la publication sur Internet",
				goal="Examinez l'offre d'emploi pour en vérifier la clarté, l'engagement, l'exactitude grammaticale et l'adéquation avec les valeurs de l'entreprise, puis affine-la pour en assurer la perfection.",
				tools=[web_search_tool, seper_dev_tool, file_read_tool],
				backstory="Tu es un rédacteur méticuleux, soucieux du détail, qui veille à ce que chaque élément de contenu soit clair, attrayant et grammaticalement parfait.",
				verbose=True,
            	step_callback=streamlit_callback,
			)
