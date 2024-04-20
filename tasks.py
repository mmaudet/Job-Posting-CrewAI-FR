from textwrap import dedent
from crewai import Task

class Tasks():
		def research_company_culture_task(self, agent, company_description, company_domain):
				return Task(
						description=dedent(f"""\
								Analysez le site web de l'entreprise et le secgeur d'activité (marché, concurrence,...) de l'entreprise {company_domain}, dont la description détaillée est la suivante  : "{company_description}". Concentrez-vous sur la compréhension de la culture, des valeurs et de la mission de l'entreprise. Identifiez les arguments de différenciation uniques et les projets ou réalisations spécifiques mis en avant sur le site.
								Rédiger un rapport résumant ces informations et expliquant comment elles peuvent être exploitées dans une offre d'emploi afin d'attirer les bons candidats."""),
						expected_output=dedent("""\
								Un rapport complet détaillant la culture, les valeurs et la mission de l'entreprise, ainsi que des arguments de différenciation spécifiques en rapport avec le poste à pourvoir. Des suggestions sur l'intégration différenciate et pertucante de ces éléments dans l'offre d'emploi doivent être incluses."""),
						agent=agent
				)

		def research_role_requirements_task(self, agent, hiring_needs):
				return Task(
						description=dedent(f"""\
								En fonction des besoins du responsable du recrutement : "{hiring_needs}", identifiez les compétences, expériences et qualités clés que le candidat idéal devrait posséder pour le poste. Tenez compte des projets actuels de l'entreprise, de son environnement concurrentiel et des tendances du secteur. Préparez une liste d'exigences et de qualifications recommandées pour le poste qui correspondent aux besoins et aux valeurs de l'entreprise."""),
						expected_output=dedent("""\
								Une liste des compétences, expériences et qualités indispensables du candidat idéal, en accord avec la culture de l'entreprise, les projets en cours et les exigences spécifiques du poste."""),
						agent=agent
				)

		def draft_job_posting_task(self, agent, company_description, hiring_needs, specific_benefits):
				return Task(
						description=dedent(f"""\
								Rédiger une offre d'emploi percutante et différenciante pour le rôle décrit par le responsable du recrutement : "{hiring_needs}". Utilisez les informations sur "{company_description}" pour commencer par une introduction convaincante, suivie d'une description détaillée du poste, des responsabilités et des compétences et qualifications requises. Veillez à ce que le ton corresponde à la culture de l'entreprise et intégrez les avantages ou les opportunités uniques offerts par l'entreprise.
								Avantages spécifiques : "{specific_benefits}"""),
						expected_output=dedent("""\
								Une offre d'emploi détaillée et attrayante comprenant une introduction, une description du rôle, des responsabilités, des exigences et des avantages uniques de l'entreprise. Le ton doit être en accord avec la culture et les valeurs de l'entreprise, afin d'attirer les bons candidats."""),
						agent=agent
				)

		def review_and_edit_job_posting_task(self, agent, hiring_needs):
				return Task(
						description=dedent(f"""\
								Examinez le projet d'offre d'emploi pour le poste : "{hiring_needs}". Vérifiez la clarté, l'engagement, l'exactitude grammaticale et l'alignement sur la culture et les valeurs de l'entreprise. Modifiez et affinez le contenu, en veillant à ce qu'il s'adresse directement aux candidats recherchés et qu'il reflète fidèlement les avantages et les possibilités uniques du poste. Fournir la révision nécessaire afin d'obtenir une offre d'emploi appelant à l'action pour le candidat qui prendre connaissance de l'offre d'emploi."""),
						expected_output=dedent("""\
								Une offre d'emploi soignée et exempte d'erreurs, claire, attrayante et en parfaite adéquation avec la culture et les valeurs de l'entreprise. Retour d'information sur les améliorations possibles et approbation finale de la publication. Résultat attendu au format markdown."""),
						agent=agent,
						output_file="offre-emploi.md"
				)

		def industry_analysis_task(self, agent, company_domain, company_description):
				return Task(
						description=dedent(f"""\
								Effectuer une analyse approfondie du secteur d'activité lié au domaine de l'entreprise : "{company_domain}". Étudier les tendances actuelles, les défis et les opportunités au sein de cette industrie, en utilisant des rapports de marché, des développements récents et des avis d'experts. Évaluez l'impact que ces facteurs pourraient avoir sur le poste à pourvoir et sur l'attrait global du poste pour les candidats potentiels.
								Bien prendre en compte la manière dont l'entreprise assure son leadership sur son marché et ses réponses aux tendances pourraient être mises à profit pour attirer les meilleurs talents. Indiquez dans votre analyse comment le profil recherché contribue à relever les défis du secteur ou à saisir les opportunités."""),
						expected_output=dedent("""\
								Un rapport d'analyse détaillé qui identifie les principales tendances, les défis et les opportunités du secteur en rapport avec le domaine de l'entreprise et la fonction spécifique recherchée. Ce rapport doit fournir des indications stratégiques sur le positionnement du poste et de l'entreprise en tant que choix attractifs pour les candidats potentiels."""),
						agent=agent
				)
