from langchain.prompts import PromptTemplate
from langchain.chat_models import ChatOpenAI, ChatAnthropic
from langchain.chains import LLMChain

from agents.linkedin_lookup_agent import lookup as linkedin_lookup_agent
#from agents.twitter_lookup_agent import lookup as twitter_lookup_agent

from third_parties.linkedin import gist_linkedin_profile_filtered, scrape_linkedin_profile
#from third_parties.twitter import scrape_user_tweets
def ice_break(name:str)->str:
    linkedin_profile_url = linkedin_lookup_agent(name="Andrey Kumskov BIM")
    linkedin_data = scrape_linkedin_profile(linkedin_profile_url=linkedin_profile_url)
#    twitter_username = twitter_lookup_agent(name=name)
#    tweets = scrape_user_tweets(username=twitter_username, num_tweets=5)

    summary_template = """
    given the Linkedin information {information} about a person from I want you to create:
    1. a short summary  
    2. two interesting facts about them  
    3. A topic interesting fact about them
    4. 2 creative Ice breakers to open a conversation with them
    """
    summary_promt_template = PromptTemplate(
        input_variables=["linkedin_information","twitter_information"],
        template=summary_template
    )

    llm = ChatAnthropic()
    # llm = ChatOpenAI()
    chain = LLMChain(llm=llm, prompt=summary_promt_template)
#    linkedin_data = gist_linkedin_profile_filtered
    result = chain.run(linkedin_information=linkedin_data)
    print(result)

if __name__ == "__main__":
    print("Hello!")
    result = ice_break(name="Harison Chase")
