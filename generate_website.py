"""
The idea is to ask the user about their website idea and their preferred backend and
frontend technologies. Then several GPT agents communicate together to create the website.

Ideas for improvements:
Teach the project lead to say the name of the party they wish to contact. E.g. if they think
that the backend needs modifications, it should say 'Backend architect' and then hit enter twice
before entering its questions/assertions. When the project lead thinks that the project is done,
it should say 'The project is done' and then provide download links, etc.
"""
import openai
import argparse
import secret_variables as sv
import yaml


class RequirementsEngineer:
    def gather_requirements(self, users_idea: str) -> str:
        # Logic to process user input and return technical requirements
        pass


class BackendArchitect:
    def design_backend(self, requirements: str, backend_choice: str) -> str:
        # Logic to design backend structure based on requirements
        pass


class FrontendArchitect:
    def design_frontend(self, requirements: str, backend_design: str, frontend_choice: str) -> str:
        # Logic to design frontend structure based on backend design
        pass


class DataModeler:
    def design_data_model(self, requirements: str, backend_design: str) -> str:
        # Logic to design the data model based on backend design
        pass


class UIUXDesigner:
    def suggest_design(self, requirements: str, frontend_design: str) -> str:
        # Logic to suggest UI/UX elements based on frontend design
        pass


def develop_website_without_project_lead(users_idea: str, be_choice: str, fe_choice: str) -> dict:
    re = RequirementsEngineer()
    ba = BackendArchitect()
    fa = FrontendArchitect()
    dm = DataModeler()
    ux = UIUXDesigner()

    requirements = re.gather_requirements(users_idea)
    backend_design = ba.design_backend(requirements, be_choice)
    frontend_design = fa.design_frontend(requirements, backend_design, fe_choice)
    data_model = dm.design_data_model(requirements, backend_design)
    design_suggestions = ux.suggest_design(requirements, frontend_design)

    return {
        "requirements": requirements,
        "backend_design": backend_design,
        "frontend_design": frontend_design,
        "data_model": data_model,
        "design_suggestions": design_suggestions
    }


class ProjectLead:
    def communicate(self, agent_title, message):
        # Communicate to a specific agent by stating their title
        return f"{agent_title}\n\n{message}"

    def conclude_project(self):
        # Conclude the project
        conclusion = "The project is done."
        return conclusion


def develop_website_with_project_lead(users_idea: str, be_choice: str, fe_choice: str) -> dict:
    re = RequirementsEngineer()
    ba = BackendArchitect()
    fa = FrontendArchitect()
    dm = DataModeler()
    ux = UIUXDesigner()
    pl = ProjectLead()

    # Sample interaction with Backend Architect through Project Lead
    pl_message = pl.communicate("Backend Architect", "What's your plan for the backend?")
    backend_response = ba.design_backend(pl.state['idea'], pl.state['backend_choice'])

    # Continue similar interactions with other agents...
    # TODO Idea: While True -loop, in it the Project Lead says something to its team member. The
    # name of the team member should be the first thing the Project Lead says. Assign the Project
    # Leads message to the desired team member. Loop breaks when the project lead starts the message
    # with: "The project is done."

    # Once done, conclude the project
    conclusion = pl.conclude_project()

    # Return the state for further actions or display
    return pl.state


def main(args: argparse.Namespace):
    if args.yml:
        with open('answers.yml', 'r') as file:
            data = yaml.safe_load(file)
        users_idea = data['users_idea']
        backend_choice = data['backend_choice']
        frontend_choice = data['frontend_choice']
    else:
        users_idea = input("Describe your website idea: ")
        backend_choice = input("Choose backend technology (e.g., Flask, Django): ")
        frontend_choice = input("Choose frontend technology (e.g., React, Vue): ")

    if args.no_pl:
        results = develop_website_without_project_lead(users_idea, backend_choice, frontend_choice)
    else:
        results = develop_website_with_project_lead(users_idea, backend_choice, frontend_choice)

    print(results)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate a website.")
    parser.add_argument('--no-pl', action='store_true', help="No project lead.")
    parser.add_argument('--yml', action='store_true', help="Read input from a YAML file.")
    args = parser.parse_args()
    main(args)
