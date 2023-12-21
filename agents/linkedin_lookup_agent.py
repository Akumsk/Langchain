from langchain.prompts import PromptTemplate
from langchain.chat_models import ChatAnthropic
from langchain.agents import initialize_agent, AgentType, Tool

from tools.tools import get_profile_url


def lookup(name: str) -> str:
    llm = ChatAnthropic()
    template = """
    given the full name {name_of_person} I want ot get it me a link to their Linked profile page.
    Your answer should contain only a URL 
    """

    tools_for_agent = [
        Tool(
            name="Crawl Google 4 linkedin profile page",
            func=get_profile_url,
            description="usefull for when you need get the Linkedin Page URL",
        )
    ]
    agent = initialize_agent(
        tools=tools_for_agent,
        llm=llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True,
    )
    prompt_template = PromptTemplate(
        template=template, input_variables=["name_of_person"]
    )

    linked_profile_url = agent.run(prompt_template.format_prompt(name_of_person=name))
    return linked_profile_url
