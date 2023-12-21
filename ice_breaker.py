from langchain.prompts import PromptTemplate
from langchain.chat_models import ChatOpenAI, ChatAnthropic
from langchain.chains import LLMChain

from agents.linkedin_lookup_agent import lookup as linkedin_lookup_agent
from third_parties.linkedin import (
    gist_linkedin_profile_filtered,
    scrape_linkedin_profile,
)

if __name__ == "__main__":
    print("Hello!")

    linkedin_profile_url = linkedin_lookup_agent(name="Andrey Kumskov BIM")

    summary_template = """
    given the Linkedin information {information} about a person from I want you to create:
    1. a short summary  
    2. two interesting facts about them  
    """

    summary_promt_template = PromptTemplate(
        input_variables=["information"], template=summary_template
    )
    llm = ChatAnthropic()
    # llm = ChatOpenAI()
    chain = LLMChain(llm=llm, prompt=summary_promt_template)

    linkedin_data = scrape_linkedin_profile(linkedin_profile_url=linkedin_profile_url)
    #    linkedin_data = gist_linkedin_profile_filtered
    print(chain.run(information=linkedin_data))
